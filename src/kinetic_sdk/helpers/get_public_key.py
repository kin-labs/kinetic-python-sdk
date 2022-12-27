# pylint: disable=missing-function-docstring,missing-module-docstring,import-error
from solana.publickey import PublicKey

from kinetic_sdk.models import PublicKeyString


def get_public_key(account: PublicKeyString) -> str:
    """Get the string representation of a PublicKey."""
    if isinstance(account, str):
        return account
    if isinstance(account, PublicKey):
        return account.to_base58().decode()

    raise TypeError("PublicKeyString must be a PublicKey or a str")
