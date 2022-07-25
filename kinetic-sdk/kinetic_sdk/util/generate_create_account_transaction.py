from spl.token.instructions import create_associated_token_account

from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.transaction import Transaction

def generate_create_account_transaction(
    add_memo: bool,
    appIndex: int,
    mint_fee_payer: str,
    mint_public_key: str,
    signer: Keypair
):
    create_transaction_instruction = create_associated_token_account(
        payer=PublicKey(mint_fee_payer), owner=signer.public_key, mint=PublicKey(mint_public_key)
    )

    transaction = Transaction()
    transaction.add(
        create_transaction_instruction
    )

    transaction.sign_partial(signer)

    return transaction.serialize()
