# pylint: disable=missing-function-docstring,missing-module-docstring,no-name-in-module
from based58 import b58decode, b58encode


def base58_encode(data: bytes) -> str:
    return b58encode(data).decode("utf-8")


def base58_decode(data: str) -> bytes:
    return b58decode(bytes(data, "utf-8"))
