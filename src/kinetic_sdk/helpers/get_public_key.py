from solana.publickey import PublicKey

from kinetic_sdk.models.public_key_string import PublicKeyString


def get_public_key(account: PublicKeyString) -> str:
    if type(account) is str:
        return account
    if type(account) is PublicKey:
        return account.to_base58().decode()
    else:
        raise "PublicKeyString must be a PublicKey or a str"
