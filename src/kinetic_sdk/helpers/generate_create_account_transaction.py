# pylint: disable=missing-function-docstring,missing-module-docstring,import-error,too-many-arguments
from solana.publickey import PublicKey
from solders.message import Message as SoldersMessage
from spl.token.instructions import AuthorityType, SetAuthorityParams, get_associated_token_address, set_authority

from kinetic_sdk.helpers.create_associated_token_account_instruction import create_associated_token_account_instruction
from kinetic_sdk.helpers.create_memo_instruction import create_memo_instruction
from kinetic_sdk.helpers.sign_and_serialize_transaction import sign_and_serialize_transaction
from kinetic_sdk.keypair import Keypair
from kinetic_sdk.models.constants import TOKEN_PROGRAM_ID


def generate_create_account_transaction(
    add_memo: bool,
    index: int,
    mint_fee_payer: str,
    mint_public_key: str,
    owner: Keypair,
    recent_blockhash: str,
):
    associated_token_account = get_associated_token_address(owner.public_key, PublicKey(mint_public_key))

    instructions = []

    if add_memo:
        instructions.append(create_memo_instruction(index))

    create_token_account_instruction = create_associated_token_account_instruction(
        payer=PublicKey(mint_fee_payer).to_solders(),
        associated_token=associated_token_account.to_solders(),
        owner=owner.public_key.to_solders(),
        mint=PublicKey(mint_public_key).to_solders(),
    )
    instructions.append(create_token_account_instruction)

    set_authority_instruction = set_authority(
        SetAuthorityParams(
            program_id=PublicKey(TOKEN_PROGRAM_ID),
            account=associated_token_account,
            authority=AuthorityType.CLOSE_ACCOUNT,
            current_authority=owner.public_key,
            new_authority=PublicKey(mint_fee_payer),
        )
    )
    instructions.append(set_authority_instruction.to_solders())

    message = SoldersMessage(instructions, owner.to_solders().pubkey())

    return sign_and_serialize_transaction(message, mint_fee_payer, owner, recent_blockhash)
