from kinetic_sdk.models.public_key_string import PublicKeyString
from solana.publickey import PublicKey


def get_public_key(account: PublicKeyString):
    if type(account) is str:
        return account
    if type(account) is PublicKey:
        return account.to_base58().decode()
    else:
        raise "PublicKeyString must be a PublicKey or a str"
