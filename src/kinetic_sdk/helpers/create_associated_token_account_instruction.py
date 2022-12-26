# pylint: disable=missing-function-docstring,missing-module-docstring,import-error
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey

from kinetic_sdk.models import (
    ASSOCIATED_TOKEN_PROGRAM_ID,
    SYSTEM_PROGRAM_PROGRAM_ID,
    SYSVAR_RENT_PUBKEY,
    TOKEN_PROGRAM_ID,
)


def create_associated_token_account_instruction(payer: Pubkey, associated_token: Pubkey, owner: Pubkey, mint: Pubkey):
    account_metas = [
        AccountMeta(payer, True, True),
        AccountMeta(associated_token, False, True),
        AccountMeta(owner, False, False),
        AccountMeta(mint, False, False),
        AccountMeta(SYSTEM_PROGRAM_PROGRAM_ID, False, False),
        AccountMeta(TOKEN_PROGRAM_ID, False, False),
        AccountMeta(SYSVAR_RENT_PUBKEY, False, False),
    ]

    return Instruction(program_id=ASSOCIATED_TOKEN_PROGRAM_ID, data=bytes(0), accounts=account_metas)
