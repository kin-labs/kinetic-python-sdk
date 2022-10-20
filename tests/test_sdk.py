from openapi_client.model.balance_response import BalanceResponse
from solana.keypair import Keypair
from kinetic_sdk import KineticSdk

from models.transaction_type import TransactionType

import logging as log

sdk = KineticSdk.setup(
    endpoint='http://localhost:3000',
    environment='devnet',
    index=1
)

mint = sdk.config.get('mint')
account_id = 'ALisrzsaVqciCxy8r6g7MUrPoRo3CpGxPhwBbZzqZ9bA'
owner = Keypair()


def test_get_balance():
    """ Test getting balance of an account """
    balance = sdk.get_balance(account_id)
    assert type(balance) == BalanceResponse
    assert int(balance['mints'][mint]) > 0


def test_get_history():
    """ Test getting history of an account """
    history = sdk.get_history(account_id, mint)
    # print(history)


def test_get_config():
    """ Test getting config of an account """
    config = sdk.config
    print(config)


def test_get_token_accounts():
    """ Test getting token accounts of an account """
    token_accounts = sdk.get_token_accounts(account_id, mint)
    print(token_accounts)


def test_request_airdrop():
    """ Test requesting airdrop for an account """
    airdrop = sdk.request_airdrop(account_id, '100', mint)
    print(airdrop)


def test_create_account():
    """ Test creating an account """
    account = sdk.create_account(owner, mint)
    print(account)


def test_make_transfer():
    """ Test making a transfer """
    alice = Keypair.from_secret_key(
        [205, 213, 7, 246, 167, 206, 37, 209, 161, 129, 168, 160, 90, 103, 198, 142, 83, 177, 214, 203, 80, 29, 71, 245,
         56, 152, 15, 8, 235, 174, 62, 79, 138, 198, 145, 111, 119, 33, 15, 237, 89, 201, 122, 89, 48, 221, 224, 71, 81,
         128, 45, 97, 191, 105, 37, 228, 243, 238, 130, 151, 53, 221, 172, 125])
    transfer = sdk.make_transfer(
        owner=alice,
        destination='BobQoPqWy5cpFioy1dMTYqNH9WpC39mkAEDJWXECoJ9y',
        amount=17,
        mint=mint,
        tx_type=TransactionType.NONE
    )
    print(transfer)
