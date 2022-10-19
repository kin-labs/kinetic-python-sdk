import kinetic_sdk

from solana.keypair import Keypair

from models.transaction_type import TransactionType

sdk = kinetic_sdk.KineticSdk.setup(
    endpoint='http://localhost:3000',
    environment='devnet',
    index=1
)

mint = sdk.config.get('mint')

account_id = 'ALisrzsaVqciCxy8r6g7MUrPoRo3CpGxPhwBbZzqZ9bA'

print('***** BALANCE ******')
balance = sdk.get_balance(account_id)
print(balance)
print('***********')
print()

print('***** OWNER PUB KEY ******')
owner = Keypair()
print(owner.public_key)
print('***********')

print('***** HISTORY ******')
history = sdk.get_history(account_id, mint)
# print(history)
print('***********')

print('***** TOKEN ACCOUNTS ******')
token_accounts = sdk.get_token_accounts(account_id, mint)
print(token_accounts)
print('***********')

print('***** REQUEST AIRDROP *****')
airdrop = sdk.request_airdrop(account_id, '14', mint)
print(airdrop)
print('***********')

print('***** ACCOUNT CREATION ******')
account = sdk.create_account(owner, mint)
print(account)
print('***********')

print('***** MAKE TRANSFER ******')
alice = Keypair.from_secret_key([205,213,7,246,167,206,37,209,161,129,168,160,90,103,198,142,83,177,214,203,80,29,71,245,56,152,15,8,235,174,62,79,138,198,145,111,119,33,15,237,89,201,122,89,48,221,224,71,81,128,45,97,191,105,37,228,243,238,130,151,53,221,172,125])
tx = sdk.make_transfer(owner=alice, destination='BobQoPqWy5cpFioy1dMTYqNH9WpC39mkAEDJWXECoJ9y', amount=17, mint=mint, tx_type=TransactionType.NONE)
print(tx)
print('***********')
