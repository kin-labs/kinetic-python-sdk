import base64

from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.instructions import transfer, get_associated_token_address, TransferParams, create_associated_token_account

from spl.memo.constants import MEMO_PROGRAM_ID
from spl.memo.instructions import create_memo, MemoParams

from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.transaction import Transaction
# from solders.transaction import Transaction

from models.transaction_type import TransactionType
from models.public_key_string import PublicKeyString

from helpers.create_kin_memo import create_kin_memo

# from solders.message import Message
# from solders.keypair import Keypair
# from solders.instruction import Instruction, AccountMeta
# from solders.hash import Hash
# from solders.transaction import Transaction
# from solders.pubkey import Pubkey
# from solders.null_signer import NullSigner

from models.layouts import (
    InstructionType,
    SYSTEM_INSTRUCTIONS_LAYOUT,
    SYSTEM_PROGRAM_ID
)


def generate_make_transfer_transaction(
    amount: int,
    add_memo: bool,
    app_index: int,
    recent_blockhash: str,
    destination: PublicKeyString,
    mint_fee_payer: str,
    mint_public_key: str,
    owner: Keypair,
    tx_type: TransactionType = TransactionType.NONE,
    sender_create: bool = False
):

    # Fee Payer
    # secret_key_signer = base64.b64decode(
    #     "2L1KkefcqtLAa3f3y9rWHhAdqXVUEqz5KmU2PZSurteYZC6Zt29yPMB6rruafuF4wZX3TmKcS3fAXX5zQcCiJA4Q"
    # )
    # secret_key_signer = b"2L1KkefcqtLAa3f3y9rWHhAdqXVUEqz5KmU2PZSurteYZC6Zt29yPMB6rruafuF4wZX3TmKcS3fAXX5zQcCiJA4Q"
    # print('secret_key_signer: ', secret_key_signer)
    # signer = Keypair.from_secret_key(secret_key_signer)
    # print('signer: ', signer.public_key)
    # signer_pubkey = PublicKey(signer.public_key)
    # print('signer_pubkey: ', signer_pubkey)

    # Fee Payer Key
    print('mint_fee_payer: ', mint_fee_payer)
    fee_payer_key = PublicKey(mint_fee_payer)

    # Mint Key
    mint_pubkey = PublicKey(mint_public_key)
    print('mint_pubkey: ', mint_pubkey)

    #  Get TokenAccount from Owner and Destination
    owner_pubkey = PublicKey(owner.public_key)
    print('owner_pubkey: ', owner_pubkey)
    owner_token_account = get_associated_token_address(
        owner_pubkey, mint_pubkey)
    print('owner_token_account: ', owner_token_account)

    destination_pubkey = PublicKey(destination)
    print('destination_pubkey: ', destination_pubkey)
    destination_token_account = get_associated_token_address(
        destination_pubkey, mint_pubkey)
    print('destination_token_account: ', destination_token_account)

    # Create Transaction
    transaction = Transaction(
        recent_blockhash=recent_blockhash, fee_payer=fee_payer_key)
    print('transaction raw: ', transaction)

    # Memo
    if (add_memo):
        memo_params = MemoParams(
            program_id=MEMO_PROGRAM_ID,
            signer=(fee_payer_key),
            message=create_kin_memo(app_index, tx_type),
        )
        transaction.add(create_memo(memo_params))

    # Setting Fee Payer
    create_transaction_instruction = create_associated_token_account(
        payer=fee_payer_key, owner=owner_pubkey, mint=mint_pubkey
    )
    print('create_transaction_instruction: ', create_transaction_instruction)
    transaction.add(
        create_transaction_instruction
    )
    print('transaction with create instruction: ', transaction)

    # Sender Create
    if (sender_create):
        # TODO
        print('sender_create: ', sender_create)

    transaction.add(
        transfer(
            TransferParams(
                program_id=TOKEN_PROGRAM_ID,
                source=owner_token_account,
                dest=destination_token_account,
                owner=owner_pubkey,
                amount=amount,
                signers=[]
            )
        )
    )
    # signers=[signer_pubkey, owner_pubkey, mint_pubkey]

    transaction.sign_partial(owner)
    print('transaction signed: ', transaction)

    return transaction.serialize(False)

    # transaction_bytes = transaction.encode()
    # print('transaction_bytes: ', transaction_bytes)

    # return bytes(transaction)
