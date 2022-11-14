from kinetic_sdk.generated.client.model.balance_response import BalanceResponse
from kinetic_sdk.generated.client.model.balance_token import BalanceToken
from kinetic_sdk.generated.client.model.history_response import HistoryResponse
from kinetic_sdk.generated.client.model.request_airdrop_response import RequestAirdropResponse
from kinetic_sdk.generated.client.model.transaction import Transaction
from kinetic_sdk.generated.client.model.transaction_status import TransactionStatus
from solana.publickey import PublicKey

from kinetic_sdk import KineticSdk
from kinetic_sdk.models.keypair import Keypair

sdk = KineticSdk.setup(
    endpoint='http://localhost:3000',
    environment='local',
    index=1
)

alice = Keypair.from_byte_array(
    [205, 213, 7, 246, 167, 206, 37, 209, 161, 129, 168, 160, 90, 103, 198, 142, 83, 177, 214, 203, 80, 29, 71, 245,
     56, 152, 15, 8, 235, 174, 62, 79, 138, 198, 145, 111, 119, 33, 15, 237, 89, 201, 122, 89, 48, 221, 224, 71, 81,
     128, 45, 97, 191, 105, 37, 228, 243, 238, 130, 151, 53, 221, 172, 125])

mint = sdk.config.get('mint')
account = 'ALisrzsaVqciCxy8r6g7MUrPoRo3CpGxPhwBbZzqZ9bA'
fee_payer = 'oWNEYV3aMze3CppdgyFAiEj9xUJXkn85es1KscRHt8m'
owner = Keypair.random()


def test_get_balance():
    """ Test getting balance of an account """
    balance = sdk.get_balance(PublicKey(account))
    # print(balance)
    assert type(balance) == BalanceResponse
    assert type(balance.balance) == str
    assert type(balance.tokens) == list
    assert type(balance.tokens[0]) == BalanceToken
    assert type(balance.mints) == dict
    assert type(balance.mints[mint]) == str


def test_get_config():
    """ Test getting config of an account """
    config = sdk.config
    print(config)
    assert type(config) == dict
    assert type(config.get('endpoint')) == str
    assert type(config.get('environment')) == str
    assert type(config.get('index')) == int


def test_get_explorer_url():
    """ Test getting explorer url """
    url = sdk.get_explorer_url('account/' + account)
    # print(url)
    assert url == 'https://explorer.solana.com/account/' + account + '?cluster=custom&customUrl=http%3A%2F%2Flocalhost%3A8899'


def test_get_history():
    """ Test getting history of an account """
    history = sdk.get_history(account)
    # print(history)
    assert type(history) == list
    assert type(history[0]) == HistoryResponse


def test_get_token_accounts():
    """ Test getting token accounts of an account """
    token_accounts = sdk.get_token_accounts(account)
    # print(token_accounts)
    assert type(token_accounts) == list


def test_request_airdrop():
    """ Test requesting airdrop for an account """
    airdrop = sdk.request_airdrop(account, "100")
    # print(airdrop)
    assert type(airdrop) == RequestAirdropResponse


def test_create_account():
    """ Test creating an account """
    created = sdk.create_account(owner)
    # print(created)
    assert type(created) == Transaction
    assert created['amount'] is None
    assert str(created['commitment']) == 'Confirmed'
    assert created['destination'] is None
    assert created['errors'] == []
    assert created['fee_payer'] == fee_payer
    assert created['mint'] == mint
    assert type(created['status']) == TransactionStatus
    assert str(created['status']) == 'Committed'


def test_make_transfer():
    """ Test making a transfer """
    transfer = sdk.make_transfer(
        owner=alice,
        destination='BobQoPqWy5cpFioy1dMTYqNH9WpC39mkAEDJWXECoJ9y',
        amount=17,
    )
    assert type(transfer) == Transaction
    assert transfer['amount'] == '17'
    assert str(transfer['commitment']) == 'Confirmed'
    assert transfer['destination'] == '92gcR7aBdZDGvoC1cCSTSzQDediBZecy32B43mJtuUXT'
    assert transfer['errors'] == []
    assert transfer['fee_payer'] == fee_payer
    assert transfer['mint'] == mint
    assert type(transfer['status']) == TransactionStatus
    assert str(transfer['status']) == 'Committed'
    assert transfer['source'] == 'ALisrzsaVqciCxy8r6g7MUrPoRo3CpGxPhwBbZzqZ9bA'


def test_make_transfer_batch():
    """ Test making a batch transfer """
    transferBatch = sdk.make_transfer_batch(
        owner=alice,
        destinations=[
            {'destination': 'BobQoPqWy5cpFioy1dMTYqNH9WpC39mkAEDJWXECoJ9y', 'amount': '12'},
            {'destination': 'CharYfTvJSiH6LtDpkGUiVVZmeCn5Cenu2TzdJSbDJnG', 'amount': '15'}
        ]
    )
    # print(transferBatch)
    assert type(transferBatch) == Transaction
    assert transferBatch['amount'] == '12'
    assert str(transferBatch['commitment']) == 'Confirmed'
    assert transferBatch['destination'] == '92gcR7aBdZDGvoC1cCSTSzQDediBZecy32B43mJtuUXT'
    assert transferBatch['errors'] == []
    assert transferBatch['fee_payer'] == fee_payer
    assert transferBatch['mint'] == mint
    assert type(transferBatch['status']) == TransactionStatus
    assert str(transferBatch['status']) == 'Committed'
    assert transferBatch['source'] == 'ALisrzsaVqciCxy8r6g7MUrPoRo3CpGxPhwBbZzqZ9bA'


# FIXME: testing this gives errors. We should revise this after the generated openapi code has been updated.
# def test_get_transaction():
#     """ Test getting transaction """
#     newTransfer = sdk.make_transfer(
#         owner=alice,
#         destination='BobQoPqWy5cpFioy1dMTYqNH9WpC39mkAEDJWXECoJ9y',
#         amount=1,
#         commitment=Commitment('Finalized')
#     )
#     # print(newTransfer)
#     # print(newTransfer['signature'])
#     tx = sdk.get_transaction(signature=newTransfer['signature'])
