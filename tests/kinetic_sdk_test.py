from kinetic_sdk.generated.client.model.app_config import AppConfig
from kinetic_sdk.generated.client.model.account_info import AccountInfo
from kinetic_sdk.generated.client.model.balance_response import BalanceResponse
from kinetic_sdk.generated.client.model.balance_token import BalanceToken
from kinetic_sdk.generated.client.model.cluster_type import ClusterType
from kinetic_sdk.generated.client.model.commitment import Commitment
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
    index=1,
    headers=[{ 'kinetic-extra-header': 4 }]
)

alice_key = [205, 213, 7, 246, 167, 206, 37, 209, 161, 129, 168, 160, 90, 103, 198, 142, 83, 177, 214, 203, 80, 29, 71, 245,
     56, 152, 15, 8, 235, 174, 62, 79, 138, 198, 145, 111, 119, 33, 15, 237, 89, 201, 122, 89, 48, 221, 224, 71, 81,
     128, 45, 97, 191, 105, 37, 228, 243, 238, 130, 151, 53, 221, 172, 125]
alice_keypair = Keypair.from_byte_array(alice_key)
alice_account = 'ALisrzsaVqciCxy8r6g7MUrPoRo3CpGxPhwBbZzqZ9bA'
alice_token_account = 'Ebq6K7xVh6PYQ8DrTQnD9fC91uQiyBMPGSV6JCG6GPdD'

bob_account = 'BobQoPqWy5cpFioy1dMTYqNH9WpC39mkAEDJWXECoJ9y'
bob_token_account = '92gcR7aBdZDGvoC1cCSTSzQDediBZecy32B43mJtuUXT'
charlie_account = 'CharYfTvJSiH6LtDpkGUiVVZmeCn5Cenu2TzdJSbDJnG'

default_mint = sdk.config.get('mint').get('public_key')

fee_payer = 'oWNEYV3aMze3CppdgyFAiEj9xUJXkn85es1KscRHt8m'

def test_get_balance():
    """ Test getting balance of an account """
    balance = sdk.get_balance(PublicKey(alice_account))
    # print(balance)
    assert type(balance) == BalanceResponse
    assert type(balance.balance) == str
    assert type(balance.tokens) == list
    assert type(balance.tokens[0]) == BalanceToken
    assert type(balance.mints) == dict
    assert type(balance.mints[default_mint]) == str


def test_get_app_config():
    """ Test getting the app config """
    app_config = sdk.config
    # print(app_config)
    assert type(app_config) == AppConfig
    assert app_config['app']['index'] == 1
    assert app_config['app']['name'] == 'App 1'
    assert app_config['environment']['name'] == 'local'
    assert app_config['environment']['cluster']['id'] == 'solana-local'
    assert app_config['environment']['cluster']['name'] == 'Solana Local'
    assert app_config['environment']['cluster']['type'] == ClusterType('Custom')
    assert app_config['mint']['symbol'] == 'KIN'
    assert app_config['mint']['public_key'] == default_mint
    assert len(app_config['mints']) == 2
    assert app_config['mints'][0].symbol == 'KIN'
    assert app_config['mints'][0].public_key == default_mint


def test_get_explorer_url():
    """ Test getting explorer url """
    url = sdk.get_explorer_url('account/' + alice_account)
    # print(url)
    assert url == 'https://explorer.solana.com/account/' + alice_account + '?cluster=custom&customUrl=http%3A%2F%2Flocalhost%3A8899'


def test_get_history():
    """ Test getting history of an account """
    history = sdk.get_history(alice_account)
    # print(history)
    assert type(history) == list
    assert type(history[0]) == HistoryResponse


def test_get_token_accounts():
    """ Test getting token accounts of an account """
    token_accounts = sdk.get_token_accounts(alice_account)
    # print(token_accounts)
    assert type(token_accounts) == list


def test_request_airdrop():
    """ Test requesting airdrop for an account """
    airdrop = sdk.request_airdrop(alice_account, "100")
    # print(airdrop)
    assert type(airdrop) == RequestAirdropResponse


def test_create_account():
    """ Test creating an account """
    kp = Keypair.random()
    created = sdk.create_account(kp)
    # print(created)
    assert type(created) == Transaction
    assert created['errors'] == []
    assert created['amount'] is None
    assert str(created['commitment']) == 'Confirmed'
    assert created['destination'] is None
    assert created['fee_payer'] == fee_payer
    assert created['mint'] == default_mint
    assert type(created['status']) == TransactionStatus
    assert str(created['status']) == 'Committed'


def test_make_transfer():
    """ Test making a transfer """
    transfer = sdk.make_transfer(
        owner=alice_keypair,
        destination=bob_account,
        amount=17,
    )
    assert type(transfer) == Transaction
    assert transfer['errors'] == []
    assert transfer['amount'] == '17'
    assert transfer['commitment'] == 'Confirmed'
    assert transfer['destination'] == bob_token_account
    assert transfer['fee_payer'] == fee_payer
    assert transfer['mint'] == default_mint
    assert type(transfer['status']) == TransactionStatus
    assert transfer['status'] == TransactionStatus('Committed')
    assert transfer['source'] == alice_account


def test_make_transfer_batch():
    """ Test making a batch transfer """
    transfer_batch = sdk.make_transfer_batch(
        owner=alice_keypair,
        destinations=[
            {'destination': bob_account, 'amount': '12'},
            {'destination': charlie_account, 'amount': '15'}
        ]
    )
    # print(transfer_batch)
    assert type(transfer_batch) == Transaction
    assert transfer_batch['errors'] == []
    assert transfer_batch['amount'] == '12'
    assert transfer_batch['commitment'] == 'Confirmed'
    assert transfer_batch['destination'] == bob_token_account
    assert transfer_batch['fee_payer'] == fee_payer
    assert transfer_batch['mint'] == default_mint
    assert type(transfer_batch['status']) == TransactionStatus
    assert transfer_batch['status'] == TransactionStatus('Committed')
    assert transfer_batch['source'] == alice_account


def test_get_transaction():
    """ Test getting transaction """
    new_transfer = sdk.make_transfer(
        owner=alice_keypair,
        destination=bob_account,
        amount=1,
        commitment=Commitment('Finalized')
    )
    tx = sdk.get_transaction(signature=new_transfer['signature'])
    # print(tx)


def test_sender_crete():
    """ Test sender create """
    destination = Keypair.random()
    tx = sdk.make_transfer(
        owner=alice_keypair,
        destination=destination.public_key,
        amount=1,
        commitment=Commitment('Finalized'),
        sender_create=True
    )
    # print(tx['signature'])

def test_get_account_info():
    """ Test getting account info """
    account_info = sdk.get_account_info(alice_account)
    # print(account_info)
    assert type(account_info) == AccountInfo
    assert type(account_info['is_mint']) == bool
    assert type(account_info['is_owner']) == bool
    assert type(account_info['is_token_account']) == bool
    assert type(account_info['tokens']) == list
    assert account_info['tokens'][0].account == alice_token_account

def test_close_account():
    """ Test closing an account """
    kp = Keypair.random()
    sdk.create_account(kp, commitment=Commitment('Finalized'))
    account_closed = sdk.close_account(
        account=str(kp.public_key),
        commitment=Commitment('Finalized')
    )
    # print(account_closed)
