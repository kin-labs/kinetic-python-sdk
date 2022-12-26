# pylint: disable=missing-function-docstring,missing-module-docstring,import-error,too-many-arguments,too-many-locals
import base64
from typing import Optional

from solana.transaction import TransactionInstruction
from solders.instruction import Instruction
from spl.memo.constants import MEMO_PROGRAM_ID

from kinetic_sdk.models.kin_memo import KinMemo
from kinetic_sdk.models.transaction_type import TransactionType


def create_memo_instruction(index: int, tx_type: Optional[TransactionType] = TransactionType.NONE) -> Instruction:
    memo: bytearray = KinMemo.new(1, tx_type, index).val
    data: bytes = base64.b64decode(memo)

    return TransactionInstruction(data=data, keys=[], program_id=MEMO_PROGRAM_ID).to_solders()
