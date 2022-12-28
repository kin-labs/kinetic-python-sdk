# pylint: disable=missing-function-docstring,missing-module-docstring,import-error,too-many-arguments,too-many-locals
import base64

from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction

from kinetic_sdk.models import KinMemo, TransactionType


def create_memo_instruction(index: int, tx_type: TransactionType) -> TransactionInstruction:
    memo: bytearray = KinMemo.new(1, tx_type, index).val
    data: bytes = base64.b64encode(memo)

    return TransactionInstruction(
        data=data, keys=[], program_id=PublicKey("Memo1UhkJRfHyvLMcVucJwxXeuD728EqVDDwQDxFMNo")
    )
