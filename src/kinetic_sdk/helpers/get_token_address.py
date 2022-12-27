# pylint: disable=missing-function-docstring,missing-module-docstring
from solana.publickey import PublicKey
from spl.token.instructions import get_associated_token_address


def get_token_address(account: str, mint: str) -> str:
    return get_associated_token_address(PublicKey(account), PublicKey(mint)).to_base58().decode("utf-8")
