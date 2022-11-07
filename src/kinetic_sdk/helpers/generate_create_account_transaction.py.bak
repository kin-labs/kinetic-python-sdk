from solana.publickey import PublicKey

from solders.instruction import AccountMeta, Instruction
from solders.message import Message as SoldersMessage
from solders.pubkey import Pubkey

from spl.token.instructions import get_associated_token_address

from kinetic_sdk.helpers.sign_and_serialize_transaction import sign_and_serialize_transaction

from kinetic_sdk.models.constants import ASSOCIATED_TOKEN_PROGRAM_ID
from kinetic_sdk.models.constants import SYSTEM_PROGRAM_PROGRAM_ID
from kinetic_sdk.models.constants import SYSVAR_RENT_PUBKEY
from kinetic_sdk.models.constants import TOKEN_PROGRAM_ID

from kinetic_sdk.models.public_key_string import PublicKeyString
from kinetic_sdk.models.keypair import Keypair


def create_associated_token_account_instruction(
        payer: Pubkey,
        associated_token: Pubkey,
        owner: Pubkey,
        mint: Pubkey):
    account_metas = [
        AccountMeta(payer, True, True),
        AccountMeta(associated_token, False, True),
        AccountMeta(owner, False, False),
        AccountMeta(mint, False, False),
        AccountMeta(SYSTEM_PROGRAM_PROGRAM_ID, False, False),
        AccountMeta(TOKEN_PROGRAM_ID, False, False),
        AccountMeta(SYSVAR_RENT_PUBKEY, False, False),
    ]

    return Instruction(
        program_id=ASSOCIATED_TOKEN_PROGRAM_ID,
        data=bytes(0),
        accounts=account_metas
    )


def generate_create_account_transaction(
        add_memo: bool,
        app_index: int,
        recent_blockhash: str,
        mint_fee_payer: PublicKeyString,
        mint_public_key: PublicKeyString,
        owner: Keypair,
):
    associated_token_account = get_associated_token_address(
        owner.public_key,
        PublicKey(mint_public_key)
    )

    instruction = create_associated_token_account_instruction(
        payer=PublicKey(mint_fee_payer).to_solders(),
        associated_token=associated_token_account.to_solders(),
        owner=owner.public_key.to_solders(),
        mint=PublicKey(mint_public_key).to_solders()
    )

    message = SoldersMessage([instruction], owner.to_solders().pubkey())

    return sign_and_serialize_transaction(message, mint_fee_payer, owner, recent_blockhash)
