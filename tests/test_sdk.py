from openapi_client.model.balance_response import BalanceResponse
from solana.keypair import Keypair
from kinetic_sdk import KineticSdk

import logging as log

sdk = KineticSdk.setup('devnet', 1)

mint = 'KinDesK3dYWo3R2wDk6Ucaf31tvQCCSYyL8Fuqp33GX'

account_id = 'ALisrzsaVqciCxy8r6g7MUrPoRo3CpGxPhwBbZzqZ9bA'

def test_get_balance():
    """ Test getting balance of an account """
    balance = sdk.get_balance(account_id)
    assert type(balance) == BalanceResponse
    assert int(balance['mints'][mint]) > 0

def test_get_history():
    """ Test getting history of an account """
    history = sdk.get_history(account_id, mint)
    print(history)
