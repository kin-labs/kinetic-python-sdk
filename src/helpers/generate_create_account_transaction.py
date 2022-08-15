from spl.token.instructions import create_associated_token_account

from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.transaction import Transaction
from models.public_key_string import PublicKeyString

def generate_create_account_transaction(
    add_memo: bool,
    appIndex: int,
    mint_fee_payer: PublicKeyString,
    mint_public_key: PublicKeyString,
    signer: Keypair
):
    payer = Keypair.generate()

    create_transaction_instruction = create_associated_token_account(
        payer=payer.public_key, owner=signer.public_key, mint=PublicKey(mint_public_key)
    )

    transaction = Transaction()
    transaction.add(
        create_transaction_instruction
    )

    tx_hash = transaction.serialize_message()

    transaction.add_signature(payer.public_key, payer.sign(tx_hash))

    transaction.sign_partial(payer)

    return transaction.serialize()
