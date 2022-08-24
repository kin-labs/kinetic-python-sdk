from spl.token.instructions import create_associated_token_account

from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.transaction import Transaction
from models.public_key_string import PublicKeyString

def generate_create_account_transaction(
    add_memo: bool,
    appIndex: int,
    recent_blockhash: str,
    mint_fee_payer: PublicKeyString,
    mint_public_key: PublicKeyString,
    signer: Keypair
):
    transaction = Transaction(recent_blockhash)

    transaction.add(
        create_associated_token_account(
            payer=signer.public_key, owner=PublicKey(mint_fee_payer), mint=PublicKey(mint_public_key)
        )
    )

    transaction.sign_partial(signer)

    return transaction.serialize()
