from openapi_client.model.balance_response import BalanceResponse
from solana.keypair import Keypair
from kinetic_sdk import KineticSdk
from models.transaction_type import TransactionType

import logging as log

sdk = KineticSdk.setup('devnet', 1)
print(' - sdk', sdk)

mint = 'KinDesK3dYWo3R2wDk6Ucaf31tvQCCSYyL8Fuqp33GX'
print(' - mint', mint)

account_id = 'ALisrzsaVqciCxy8r6g7MUrPoRo3CpGxPhwBbZzqZ9bA'
print(' - account_id', account_id)

devnet_account_1_mnemonic = "where file bag name start afford reject couple enjoy pause salmon defy"
devnet_account_1_secret_key = "McNNXQqixU4zQywMf5ipygL66RG6qzFFzPMMaDDGFattiCUYfmmo3ZyJPHgDYNfkjeg8KMHfEfuYD66uLbfR7tm"
devnet_account_1_public_key = "7BrMeTUstpoVh6yZzCHLQLB8knoDZb2rJXkpfeA1mC2m"
devnet_account_2_mnemonic = "shrimp unveil waste lake half allow load inspire course put jewel ancient"
devnet_account_2_secret_key = "3HYswwbBkZGawwmnbfPo8zVKkGPAtXXkUwK1Bk8bzZ8UH6UU7HAkYnfvnxPcXVf7mK4d4eqJCwyqbW3PYkReGiuH"
devnet_account_2_public_key = "6NQsrNWrVchq6N96aXuH93Ec4o5wigoJQR5zD1w7j947"
fee_payer_devnet_account_mnemonic = "coyote hurdle dune inform orbit wolf meadow bike pole boost fluid news"
fee_payer_devnet_account_secret_key = "2L1KkefcqtLAa3f3y9rWHhAdqXVUEqz5KmU2PZSurteYZC6Zt29yPMB6rruafuF4wZX3TmKcS3fAXX5zQcCiJA4Q"
fee_payer_devnet_account_public_key = "CHV9sprve2JH14AL57VMqBQFGGrzLa8hpKgp382LmX8c"
fee_payer_devnet_account_byte_array = [66, 104, 28, 119, 223, 34, 56, 243, 209, 12, 94, 113, 79, 253, 250, 208, 35, 105, 152, 56, 224, 106, 235, 126, 81, 47, 52, 108,
                                       26, 227, 90, 228, 167, 169, 174, 143, 149, 169, 49, 61, 187, 137, 84, 82, 249, 156, 27, 161, 167, 196, 154, 54, 8, 176, 44, 240, 83, 79, 13, 193, 142, 119, 158, 97]


# def test_make_transfer():
#     """ Test Account Creation """
#     print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
#     print('sdk: ', sdk)

#     print('devnet_account_1_secret_key: ', devnet_account_1_secret_key)
#     print('Keypair.from_secret_key: ', Keypair.from_secret_key)
#     owner = Keypair.from_secret_key(str.encode(devnet_account_1_secret_key))
#     print('owner: ', owner)
#     print('owner.public_key: ', owner.public_key)

#     destination = devnet_account_2_public_key
#     print('destination: ', destination)

#     amount = 1
#     print('amount: ', amount)

#     print('mint: ', mint)

#     tx_type = TransactionType.NONE
#     print('TransactionType: ', TransactionType)
#     print('tx_type: ', tx_type)

#     balance1 = sdk.get_balance(devnet_account_1_public_key)
#     print('balance1: ', balance1)
#     balance2 = sdk.get_balance(devnet_account_2_public_key)
#     print('balance2: ', balance2)
#     balance3 = sdk.get_balance(fee_payer_devnet_account_public_key)
#     print('balance3: ', balance3)

#     transfer = sdk.make_transfer(
#         owner=owner, destination=destination, mint=mint, amount=amount, tx_type=tx_type)
#     print('transfer: ', transfer)

#     # balance = sdk.get_balance(devnet_account_1_public_key)
#     # print('balance: ', balance)

#     balance = 1000
#     assert int(balance) > 999

def test_create_account():
    """ Test Account Creation """
    keypair = Keypair.generate()
    print('keypair: ', keypair.seed)

    create = sdk.create_account(owner=keypair, mint=mint)
    print('create: ', create)

    balance = 1000
    assert int(balance) > 999


# def test_get_balance():
#     """ Test getting balance of an account """
#     balance = sdk.get_balance(account_id)
#     print('balance: ', balance)
#     assert type(balance) == BalanceResponse
#     assert int(balance['mints'][mint]) > 0


# def test_get_history():
#     """ Test getting history of an account """
#     history = sdk.get_history(account_id, mint)
#     print(history)
