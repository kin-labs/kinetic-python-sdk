# pylint: disable=missing-function-docstring,missing-module-docstring,import-error
from solana.publickey import PublicKey
from solana.transaction import Transaction
from solders.hash import Hash
from solders.transaction import Transaction as SoldersTransaction


def sign_and_serialize_transaction(message, mint_fee_payer, owner, recent_blockhash):
    solders_transaction = SoldersTransaction.new_unsigned(message)
    transaction = Transaction.from_solders(solders_transaction)
    transaction.fee_payer = PublicKey(mint_fee_payer)
    solders_transaction = transaction.to_solders()
    solders_transaction.partial_sign([owner.to_solders()], Hash.from_string(recent_blockhash))
    transaction = Transaction.from_solders(solders_transaction)
    return transaction.serialize(verify_signatures=False)
