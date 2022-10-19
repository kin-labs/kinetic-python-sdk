from solana.publickey import PublicKey
from solana.transaction import Transaction

from solders.hash import Hash
from solders.instruction import AccountMeta, Instruction
from solders.message import Message as SoldersMessage
from solders.pubkey import Pubkey
from solders.transaction import Transaction as SoldersTransaction

from spl.token._layouts import INSTRUCTIONS_LAYOUT, InstructionType
from spl.token.instructions import get_associated_token_address

from models.public_key_string import PublicKeyString
from models.transaction_type import TransactionType

TOKEN_PROGRAM_ID = Pubkey.from_string("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA")
ASSOCIATED_TOKEN_PROGRAM_ID = Pubkey.from_string('ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL')
SYSTEM_PROGRAM_PROGRAM_ID = Pubkey.from_string('11111111111111111111111111111111')
SYSVAR_RENT_PUBKEY = Pubkey.from_string("SysvarRent111111111111111111111111111111111")


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

    data = INSTRUCTIONS_LAYOUT.build(
        dict(instruction_type=InstructionType.TRANSFER2, args=dict(amount=amount, decimals=decimals))
    )

    return Instruction(
        program_id=TOKEN_PROGRAM_ID,
        data=data,
        accounts=account_metas
    )


def generate_make_transfer_transaction(
    add_memo: bool,
    app_index: int,
    amount: int,
    destination: PublicKeyString,
    decimals: int,
    mint_fee_payer: str,
    mint_public_key: str,
    recent_blockhash: str,
    source,
    tx_type: TransactionType = TransactionType.NONE
):
    source_token_account = get_associated_token_address(source.public_key, PublicKey(mint_public_key))
    destination_token_account = get_associated_token_address(PublicKey(destination), PublicKey(mint_public_key))

    instruction = create_make_transfer_instruction(
        source=source.public_key.to_solders(),
        source_token_account=source_token_account.to_solders(),
        destination_token_account=destination_token_account.to_solders(),
        mint=PublicKey(mint_public_key).to_solders(),
        amount=amount,
        decimals=decimals
    )

    message = SoldersMessage([instruction], source.to_solders().pubkey())
    solders_transaction = SoldersTransaction.new_unsigned(message)

    transaction = Transaction.from_solders(solders_transaction)

    transaction.fee_payer = PublicKey(mint_fee_payer)

    solders_transaction = transaction.to_solders()

    solders_transaction.partial_sign([source.to_solders()], Hash.from_string(recent_blockhash))

    transaction = Transaction.from_solders(solders_transaction)

    return transaction.serialize(verify_signatures=False)
