from contextlib import nullcontext
from spl.token.instructions import create_associated_token_account, get_associated_token_address

from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.transaction import Transaction
from models.public_key_string import PublicKeyString


def generate_create_account_transaction(
    add_memo: bool,
    appIndex: int,
    mint_fee_payer: PublicKeyString,
    mint_public_key: PublicKeyString,
    signer: Keypair,
    recent_blockhash: str
):
    # Fee Payer Key
    print('mint_fee_payer: ', mint_fee_payer)
    fee_payer_key = PublicKey(mint_fee_payer)

    # Mint Key
    mint_key = PublicKey(mint_public_key)
    print('mint_key: ', mint_key)

    #  Get TokenAccount from Owner and Destination
    signer_key = PublicKey(signer.public_key)
    print('signer_key: ', signer_key)
    # signer_token_account = get_associated_token_address(
    #     signer_key, mint_key)
    # print('signer_token_account: ', signer_token_account)

    transaction = Transaction(
        recent_blockhash=recent_blockhash, fee_payer=fee_payer_key)
    transaction.add(
        create_associated_token_account(
            payer=fee_payer_key, owner=signer_key, mint=mint_key
        )
    )

    # transaction.add_signature(pubkey=signer_key, signature=None)

    transaction.sign_partial(signer)

    return transaction.serialize()
