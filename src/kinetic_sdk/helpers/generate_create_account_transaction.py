# pylint: disable=missing-function-docstring,missing-module-docstring,import-error,too-many-arguments
from solana.publickey import PublicKey
from solders.instruction import Instruction
from solders.message import Message as SoldersMessage
from spl.token.instructions import AuthorityType, SetAuthorityParams, set_authority

from kinetic_sdk.helpers.create_associated_token_account_instruction import create_associated_token_account_instruction
from kinetic_sdk.helpers.create_memo_instruction import create_memo_instruction
from kinetic_sdk.helpers.sign_and_serialize_transaction import sign_and_serialize_transaction
from kinetic_sdk.keypair import Keypair
from kinetic_sdk.models import TOKEN_PROGRAM_ID, TransactionType


def generate_create_account_transaction(
    add_memo: bool,
    blockhash: str,
    index: int,
    mint_fee_payer: str,
    mint_public_key: str,
    owner: Keypair,
    owner_token_account: str,
):
    mint_key = PublicKey(mint_public_key)
    fee_payer_key = PublicKey(mint_fee_payer)
    owner_public_key = owner.public_key
    owner_token_account_public_key = PublicKey(owner_token_account)

    # Create Instructions
    instructions: list[Instruction] = []

    # Create the Memo Instruction
    if add_memo:
        instructions.append(create_memo_instruction(index=index, tx_type=TransactionType.NONE).to_solders())

    create_token_account_instruction = create_associated_token_account_instruction(
        payer=fee_payer_key.to_solders(),
        associated_token=owner_token_account_public_key.to_solders(),
        owner=owner_public_key.to_solders(),
        mint=mint_key.to_solders(),
    )
    instructions.append(create_token_account_instruction)

    set_authority_instruction = set_authority(
        SetAuthorityParams(
            program_id=PublicKey(TOKEN_PROGRAM_ID),
            account=owner_token_account_public_key,
            authority=AuthorityType.CLOSE_ACCOUNT,
            current_authority=owner_public_key,
            new_authority=fee_payer_key,
        )
    )
    instructions.append(set_authority_instruction.to_solders())

    message = SoldersMessage(instructions, owner.to_solders().pubkey())

    return sign_and_serialize_transaction(message, mint_fee_payer, owner, blockhash)
