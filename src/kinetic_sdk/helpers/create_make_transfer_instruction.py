# pylint: disable=missing-function-docstring,missing-module-docstring,import-error,too-many-arguments,too-many-locals
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey
from spl.token._layouts import INSTRUCTIONS_LAYOUT, InstructionType

from kinetic_sdk.models import TOKEN_PROGRAM_ID


def create_make_transfer_instruction(
    owner: Pubkey,
    owner_token_account: Pubkey,
    destination_token_account: Pubkey,
    mint: Pubkey,
    amount: int,
    decimals: int,
):
    account_metas = [
        AccountMeta(owner_token_account, False, True),
        AccountMeta(mint, False, False),
        AccountMeta(destination_token_account, False, True),
        AccountMeta(owner, True, False),
    ]

    amount = amount * 10**decimals
    data = INSTRUCTIONS_LAYOUT.build(
        dict(instruction_type=InstructionType.TRANSFER2, args=dict(amount=amount, decimals=decimals))
    )

    return Instruction(program_id=TOKEN_PROGRAM_ID, data=data, accounts=account_metas)
