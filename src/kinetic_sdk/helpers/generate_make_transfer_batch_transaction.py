# pylint: disable=missing-function-docstring,missing-module-docstring,import-error,too-many-arguments,too-many-locals
from typing import Dict, List

from solana.publickey import PublicKey
from solders.instruction import Instruction
from solders.message import Message as SoldersMessage

from kinetic_sdk.helpers.create_make_transfer_instruction import create_make_transfer_instruction
from kinetic_sdk.helpers.create_memo_instruction import create_memo_instruction
from kinetic_sdk.helpers.sign_and_serialize_transaction import sign_and_serialize_transaction
from kinetic_sdk.keypair import Keypair
from kinetic_sdk.models import TransactionType


def generate_make_transfer_batch_transaction(
    add_memo: bool,
    blockhash: str,
    destinations: List[Dict[str, str]],
    index: int,
    mint_decimals: int,
    mint_fee_payer: str,
    mint_public_key: str,
    owner: Keypair,
    owner_token_account: str,
    tx_type: TransactionType = TransactionType.NONE,
):
    instructions: List[Instruction] = []

    # Create the Memo Instruction
    if add_memo:
        instructions.append(create_memo_instruction(index=index, tx_type=tx_type).to_solders())

    for destination in destinations:
        instruction = create_make_transfer_instruction(
            owner=owner.public_key.to_solders(),
            owner_token_account=PublicKey(owner_token_account).to_solders(),
            destination_token_account=PublicKey(destination["destination"]).to_solders(),
            mint=PublicKey(mint_public_key).to_solders(),
            amount=int(destination["amount"]),
            decimals=mint_decimals,
        )

        instructions.append(instruction)

    message = SoldersMessage(instructions, owner.to_solders().pubkey())

    return sign_and_serialize_transaction(message, mint_fee_payer, owner, blockhash)
