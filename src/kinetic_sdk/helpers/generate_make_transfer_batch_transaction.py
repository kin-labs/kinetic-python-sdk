# pylint: disable=missing-function-docstring,missing-module-docstring,import-error,too-many-arguments,too-many-locals
from typing import Dict, List

from solana.publickey import PublicKey
from solders.instruction import Instruction
from solders.message import Message as SoldersMessage
from spl.token.instructions import get_associated_token_address

from kinetic_sdk.helpers.create_make_transfer_instruction import create_make_transfer_instruction
from kinetic_sdk.helpers.create_memo_instruction import create_memo_instruction
from kinetic_sdk.helpers.sign_and_serialize_transaction import sign_and_serialize_transaction
from kinetic_sdk.keypair import Keypair
from kinetic_sdk.models.public_key_string import PublicKeyString
from kinetic_sdk.models.transaction_type import TransactionType


def generate_make_transfer_batch_transaction(
    add_memo: bool,
    destinations: List[Dict[PublicKeyString, str]],
    decimals: int,
    index: int,
    mint_fee_payer: str,
    mint_public_key: str,
    recent_blockhash: str,
    owner: Keypair,
    tx_type: TransactionType = TransactionType.NONE,
):
    instructions: List[Instruction] = []

    # Create the Memo Instruction
    if add_memo:
        instructions.append(create_memo_instruction(index=index, tx_type=tx_type))

    for destination in destinations:
        owner_token_account = get_associated_token_address(owner.public_key, PublicKey(mint_public_key))
        destination_token_account = get_associated_token_address(
            PublicKey(destination["destination"]), PublicKey(mint_public_key)
        )

        instruction = create_make_transfer_instruction(
            owner=owner.public_key.to_solders(),
            owner_token_account=owner_token_account.to_solders(),
            destination_token_account=destination_token_account.to_solders(),
            mint=PublicKey(mint_public_key).to_solders(),
            amount=int(destination["amount"]),
            decimals=decimals,
        )

        instructions.append(instruction)

    message = SoldersMessage(instructions, owner.to_solders().pubkey())

    return sign_and_serialize_transaction(message, mint_fee_payer, owner, recent_blockhash)
