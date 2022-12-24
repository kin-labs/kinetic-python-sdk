# pylint: disable=missing-class-docstring,missing-module-docstring
from enum import IntEnum


class TransactionType(IntEnum):
    UNKNOWN = -1
    NONE = 0
    EARN = 1
    SPEND = 2
    P2P = 3
