# pylint: disable=missing-function-docstring,missing-module-docstring,import-error,too-many-arguments,too-many-locals
from solana.publickey import PublicKey
from solders.instruction import Instruction
from solders.message import Message as SoldersMessage
from solders.pubkey import Pubkey

from kinetic_sdk.helpers.create_make_transfer_instruction import create_make_transfer_instruction
from kinetic_sdk.helpers.create_memo_instruction import create_memo_instruction
from kinetic_sdk.helpers.generate_create_account_transaction import create_associated_token_account_instruction
from kinetic_sdk.helpers.sign_and_serialize_transaction import sign_and_serialize_transaction
from kinetic_sdk.keypair import Keypair
from kinetic_sdk.models import TransactionType


def generate_make_transfer_transaction(
    add_memo: bool,
    amount: str,
    blockhash: str,
    destination: str,
    destination_token_account: str,
    index: int,
    mint_decimals: int,
    mint_fee_payer: str,
    mint_public_key: str,
    owner: Keypair,
    owner_token_account: str,
    sender_create,
    tx_type: TransactionType = TransactionType.NONE,
):
    # Create Instructions
    instructions: list[Instruction] = []

    # Create the Memo Instruction
    if add_memo:
        instructions.append(create_memo_instruction(index=index, tx_type=tx_type).to_solders())

    # Create the Token Account if senderCreate is enabled
    if sender_create:
        create_instruction = create_associated_token_account_instruction(
            payer=PublicKey(mint_fee_payer).to_solders(),
            associated_token=Pubkey.from_string(destination_token_account),
            owner=PublicKey(destination).to_solders(),
            mint=PublicKey(mint_public_key).to_solders(),
        )
        instructions.append(create_instruction)

    # Create the Token Transfer Instruction
    instruction = create_make_transfer_instruction(
        owner=owner.public_key.to_solders(),
        owner_token_account=Pubkey.from_string(owner_token_account),
        destination_token_account=Pubkey.from_string(destination_token_account),
        mint=PublicKey(mint_public_key).to_solders(),
        amount=int(amount),
        decimals=mint_decimals,
    )
    instructions.append(instruction)

    # Create transaction
    message = SoldersMessage(instructions, owner.to_solders().pubkey())

    # Partially sign the transaction
    return sign_and_serialize_transaction(message, mint_fee_payer, owner, blockhash)
