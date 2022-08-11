from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.instructions import transfer_checked, TransferCheckedParams

from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.transaction import Transaction

from models.transaction_type import TransactionType

def generate_make_transfer_transaction(
    amount: int,
    add_memo: bool,
    appIndex: int,
    destination: str,
    mint_fee_payer: str,
    mint_public_key: str,
    source: Keypair,
    type: TransactionType = TransactionType.NONE
):
    transaction = Transaction()
    transaction.add(
        transfer_checked(
            TransferCheckedParams(
                program_id=TOKEN_PROGRAM_ID,
                source=source.public_key,
                mint=PublicKey(mint_public_key),
                dest=PublicKey(destination),
                owner=PublicKey(mint_fee_payer),
                amount=amount,
                decimals=5,
                signers=[]
            )
        )
    )

    transaction.sign_partial(source)

    return transaction.serialize()
