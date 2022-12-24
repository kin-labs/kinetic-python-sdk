import base64

from solders.instruction import Instruction

from kinetic_sdk.models.kin_memo import KinMemo
from kinetic_sdk.models.transaction_type import TransactionType


def create_memo_instruction(index: int, tx_type: TransactionType):
    data = KinMemo.new(1, tx_type, index).val
    return Instruction(
        program_id="Memo1UhkJRfHyvLMcVucJwxXeuD728EqVDDwQDxFMNo",
        data=base64.b64encode(data).decode("utf-8"),
    )
