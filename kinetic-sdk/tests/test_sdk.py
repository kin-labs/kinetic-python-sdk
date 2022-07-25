from openapi_client.model.balance_response import BalanceResponse

from solana.keypair import Keypair

from kinetic_sdk.kinetic_sdk import KineticSdk

sdk = KineticSdk.setup('devnet', 1)

mint = 'KinDesK3dYWo3R2wDk6Ucaf31tvQCCSYyL8Fuqp33GX'

account_id = 'ALisrzsaVqciCxy8r6g7MUrPoRo3CpGxPhwBbZzqZ9bA'

from kinetic_sdk import __version__

def test_version():
    assert __version__ == '0.1.0'

def test_get_balance():
    balance = sdk.get_balance(account_id)
    assert type(balance) == BalanceResponse, "Should be TRUE"
    assert int(balance['mints'][mint]) > 0

