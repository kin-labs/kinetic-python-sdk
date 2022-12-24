from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey
from spl.token._layouts import INSTRUCTIONS_LAYOUT, InstructionType

from kinetic_sdk.models.constants import TOKEN_PROGRAM_ID


def create_make_transfer_instruction(
    source: Pubkey,
    source_token_account: Pubkey,
    destination_token_account: Pubkey,
    mint: Pubkey,
    amount: int,
    decimals: int,
):
    account_metas = [
        AccountMeta(source_token_account, False, True),
        AccountMeta(mint, False, False),
        AccountMeta(destination_token_account, False, True),
        AccountMeta(source, True, False),
    ]

    amount = amount * 10 ** decimals
    data = INSTRUCTIONS_LAYOUT.build(
        dict(instruction_type=InstructionType.TRANSFER2, args=dict(amount=amount, decimals=decimals))
    )

    return Instruction(
        program_id=TOKEN_PROGRAM_ID,
        data=data,
        accounts=account_metas
    )