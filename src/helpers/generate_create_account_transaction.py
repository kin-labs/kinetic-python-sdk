from contextlib import nullcontext
from spl.token.instructions import create_associated_token_account, get_associated_token_address

from solana.keypair import Keypair as SolanaKeypair
from solana.publickey import PublicKey as SolanaPublicKey
from solana.transaction import TransactionInstruction, Transaction
from models.public_key_string import PublicKeyString

from solders.message import Message
from solders.keypair import Keypair
from solders.instruction import Instruction, AccountMeta
from solders.hash import Hash
from solders.transaction import Transaction
from solders.pubkey import Pubkey


TOKEN_PROGRAM_ID = Pubkey.from_string(
    'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA')
ASSOCIATED_TOKEN_PROGRAM_ID = Pubkey.from_string(
    'ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL')
SYSVAR_RENT_PUBKEY = Pubkey.from_string(
    'SysvarRent111111111111111111111111111111111')
ZERO_BYTES = bytes([0])
SYS_PROGRAM_ID = Pubkey.from_string(
    '11111111111111111111111111111111')


def generate_create_account_transaction(
    add_memo: bool,
    appIndex: int,
    mint_fee_payer: PublicKeyString,
    mint_public_key: PublicKeyString,
    owner: Keypair,
    recent_blockhash: str
):
    signer = SolanaKeypair.from_secret_key(bytes([24, 20, 238, 188, 26, 234, 120, 209, 88, 63, 170, 46, 66, 98, 21, 113, 194, 120, 143, 228, 231, 37, 91, 0, 242, 32, 180, 99, 243,
                                                  179, 57, 144, 11, 233, 235, 235, 203, 20, 105, 33, 47, 140, 152, 253, 12, 148, 72, 175, 141, 253, 242, 110, 225, 110, 21, 211, 118, 87, 111, 206, 208, 166, 190, 78]))
    print('signer: ', signer.public_key)

    # Fee Payer Key
    fee_payer_key = SolanaPublicKey(mint_fee_payer)
    print('fee_payer_key: ', fee_payer_key)

    # Mint Key
    mint_key = SolanaPublicKey(mint_public_key)
    print('mint_key: ', mint_key)

    #  Get TokenAccount from Owner and Destination
    owner_key = owner.public_key
    # owner_key = PublicKey(owner.public_key)
    print('owner_key: ', owner_key)

    # owner_token_account = get_associated_token_address(
    #     owner_key, mint_key)
    # print('owner_token_account: ', owner_token_account)

    print(bytes(owner_key))
    print(bytes(mint_key))

    associated_token_address = get_associated_token_address(
        owner_key, mint_key)
    print('associated_token_address: ', associated_token_address)

    instruction = TransactionInstruction(
        keys=[
            AccountMeta(pubkey=fee_payer_key.to_solders(),
                        is_signer=True, is_writable=True),
            AccountMeta(pubkey=Pubkey.from_string(str(associated_token_address)),
                        is_signer=False, is_writable=True),
            AccountMeta(pubkey=Pubkey.from_string(str(owner_key)),
                        is_signer=False, is_writable=False),
            AccountMeta(pubkey=mint_key.to_solders(),
                        is_signer=False, is_writable=False),
            AccountMeta(pubkey=SYS_PROGRAM_ID,
                        is_signer=False, is_writable=False),
            AccountMeta(pubkey=TOKEN_PROGRAM_ID,
                        is_signer=False, is_writable=False),
            AccountMeta(pubkey=SYSVAR_RENT_PUBKEY,
                        is_signer=False, is_writable=False),
        ],
        program_id=ASSOCIATED_TOKEN_PROGRAM_ID,
    )
    print('instruction: ', instruction)

    print('recent_blockhash: ', recent_blockhash)

    transaction = Transaction(
        recent_blockhash=recent_blockhash, fee_payer=fee_payer_key)
    print('transaction raw: ', transaction)

    # transaction.add(
    #     instruction
    # )
    # print('transaction instruction: ', transaction)

    # transaction.add_signature(pubkey=owner_key, signature=None)

    transaction.sign_partial(owner)

    return transaction.serialize()
