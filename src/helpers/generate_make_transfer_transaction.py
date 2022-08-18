from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.instructions import transfer, get_associated_token_address, TransferParams

from spl.memo.constants import MEMO_PROGRAM_ID
from spl.memo.instructions import create_memo, MemoParams

# from solana.keypair import Keypair
from solana.publickey import PublicKey
# from solana.transaction import Transaction
from solders.transaction import Transaction

from models.transaction_type import TransactionType
from models.public_key_string import PublicKeyString

from helpers.create_kin_memo import create_kin_memo

from solders.message import Message
from solders.keypair import Keypair
from solders.instruction import Instruction, AccountMeta
from solders.hash import Hash
from solders.transaction import Transaction
from solders.pubkey import Pubkey

def generate_make_transfer_transaction(
    amount: int,
    add_memo: bool,
    app_index: int,
    recent_blockhash: str,
    destination: PublicKeyString,
    mint_fee_payer: str,
    mint_public_key: str,
    source,
    tx_type: TransactionType = TransactionType.NONE
):
    # transaction = Transaction(
    #     recent_blockhash
    # )

    # source_token_account = get_associated_token_address(source.public_key, PublicKey(mint_public_key))
    # destination_token_account = get_associated_token_address(PublicKey(destination), PublicKey(mint_public_key))

    # if (add_memo):
    #     memo_params = MemoParams(
    #         program_id=MEMO_PROGRAM_ID,
    #         signer=(mint_fee_payer),
    #         message=create_kin_memo(app_index, tx_type),
    #     )
    #     transaction.add(create_memo(memo_params))

    # transaction.add(
    #     transfer(
    #         TransferParams(
    #             program_id=TOKEN_PROGRAM_ID,
    #             source=source_token_account,
    #             dest=destination_token_account,
    #             owner=source.public_key,
    #             amount=amount,
    #             signers=[source.public_key, PublicKey(mint_fee_payer)]
    #         )
    #     )
    # )

    # transaction.sign_partial(source)

    # return transaction.serialize(False)

    program_id = Pubkey.default()
    arbitrary_instruction_data = bytes([1])
    accounts = []
    instruction = Instruction(program_id, arbitrary_instruction_data, accounts)
    payer = source.to_solders()
    message = Message([instruction], payer.pubkey())

    blockhash = Hash.default()

    instruction = Instruction(TOKEN_PROGRAM_ID, [AccountMeta(payer, True, True), AccountMeta(id0, True, True)])

    transaction = Transaction([payer], message, blockhash)

    # transaction = Transaction(
    #     recent_blockhash
    # )

    source_token_account = get_associated_token_address(source.public_key, PublicKey(mint_public_key))
    destination_token_account = get_associated_token_address(PublicKey(destination), PublicKey(mint_public_key))

    # if (add_memo):
    #     memo_params = MemoParams(
    #         program_id=MEMO_PROGRAM_ID,
    #         signer=(mint_fee_payer),
    #         message=create_kin_memo(app_index, tx_type),
    #     )
    #     transaction.add(create_memo(memo_params))

    transaction.add(
        transfer(
            TransferParams(
                program_id=TOKEN_PROGRAM_ID,
                source=source_token_account,
                dest=destination_token_account,
                owner=source.public_key,
                amount=amount,
                signers=[source.public_key, PublicKey(mint_fee_payer)]
            )
        )
    )

    transaction.sign_partial(source)

    return transaction.serialize(False)