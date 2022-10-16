from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.transaction import Transaction

from solders.hash import Hash
from solders.instruction import AccountMeta, Instruction
from solders.message import Message as SoldersMessage
from solders.pubkey import Pubkey
from solders.transaction import Transaction as SoldersTransaction

from spl.token.instructions import get_associated_token_address

from models.public_key_string import PublicKeyString

TOKEN_PROGRAM_ID = Pubkey.from_string("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA")
ASSOCIATED_TOKEN_PROGRAM_ID = Pubkey.from_string('ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL')
SYSTEM_PROGRAM_PROGRAM_ID = Pubkey.from_string('11111111111111111111111111111111')
SYSVAR_RENT_PUBKEY = Pubkey.from_string("SysvarRent111111111111111111111111111111111")


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
    solders_transaction = SoldersTransaction.new_unsigned(message)

    transaction = Transaction.from_solders(solders_transaction)

    transaction.fee_payer = PublicKey(mint_fee_payer)

    solders_transaction = transaction.to_solders()

    solders_transaction.partial_sign([owner.to_solders()], Hash.from_string(recent_blockhash))

    transaction = Transaction.from_solders(solders_transaction)

    return transaction.serialize(verify_signatures=False)
