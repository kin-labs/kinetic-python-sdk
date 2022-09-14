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
    owner: Keypair,
    recent_blockhash: str
):
    signer = Keypair.from_secret_key(bytes([24, 20, 238, 188, 26, 234, 120, 209, 88, 63, 170, 46, 66, 98, 21, 113, 194, 120, 143, 228, 231, 37, 91, 0, 242, 32, 180, 99, 243,
                                     179, 57, 144, 11, 233, 235, 235, 203, 20, 105, 33, 47, 140, 152, 253, 12, 148, 72, 175, 141, 253, 242, 110, 225, 110, 21, 211, 118, 87, 111, 206, 208, 166, 190, 78]))
    print('signer: ', signer.public_key)

    # Fee Payer Key
    fee_payer_key = PublicKey(mint_fee_payer)
    print('fee_payer_key: ', fee_payer_key)

    # Mint Key
    mint_key = PublicKey(mint_public_key)
    print('mint_key: ', mint_key)

    #  Get TokenAccount from Owner and Destination
    owner_key = owner.public_key
    # owner_key = PublicKey(owner.public_key)
    print('owner_key: ', owner_key)
    # owner_token_account = get_associated_token_address(
    #     owner_key, mint_key)
    # print('owner_token_account: ', owner_token_account)

    print('recent_blockhash: ', recent_blockhash)
    transaction = Transaction(
        recent_blockhash=recent_blockhash, fee_payer=fee_payer_key)

    transaction.add(
        create_associated_token_account(
            payer=fee_payer_key, owner=owner_key, mint=mint_key
        )
    )

    # transaction.add_signature(pubkey=owner_key, signature=None)

    transaction.sign_partial(owner)

    return transaction.serialize()
