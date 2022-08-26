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
from solders.null_signer import NullSigner

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
    source,
    tx_type: TransactionType = TransactionType.NONE
):
    TOKEN_PROGRAM_ID = Pubkey.from_string('TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA')
    ASSOCIATED_TOKEN_PROGRAM_ID = Pubkey.from_string('ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL')
    SYSVAR_RENT_PUBKEY = Pubkey.from_string('SysvarRent111111111111111111111111111111111')
    ZERO_BYTES = bytes([0])
    SYSTEM_PROGRAM_PROGRAM_ID = Pubkey.from_string('11111111111111111111111111111111')


    # program_id = Pubkey.default()
    # arbitrary_instruction_data = bytes([1])
    # accounts = []
    # instruction = Instruction(program_id, arbitrary_instruction_data, accounts)
    # payer = source.to_solders()
    # message = Message([instruction], payer.pubkey())

    # blockhash = Hash.default()

    # instruction = Instruction(TOKEN_PROGRAM_ID, [AccountMeta(payer, True, True), AccountMeta(id0, True, True)])

    # transaction = Transaction([payer], message, blockhash)

    # # transaction = Transaction(
    # #     recent_blockhash
    # # )

    # source_token_account = get_associated_token_address(source.public_key, PublicKey(mint_public_key))
    # destination_token_account = get_associated_token_address(PublicKey(destination), PublicKey(mint_public_key))

    # # if (add_memo):
    # #     memo_params = MemoParams(
    # #         program_id=MEMO_PROGRAM_ID,
    # #         signer=(mint_fee_payer),
    # #         message=create_kin_memo(app_index, tx_type),
    # #     )
    # #     transaction.add(create_memo(memo_params))

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

    # account_metas = [
    #     AccountMeta(keypair.pubkey(), True, True),
    #     AccountMeta(to, False, True),
    # ]
    # instruction = Instruction(program_id, bytes([1, 2, 3]), account_metas)
    # message = Message([instruction], keypair.pubkey())
    # return Transaction([keypair], message, Hash.default())


    # instruction = Instruction(TOKEN_PROGRAM_ID, [AccountMeta(payer, True, True), AccountMeta(, True, True)])


    # signersPublic = [from.publicKey, hopSignerPublicKey];

    # final instruction = TokenInstruction.transfer(
    #   source: Ed25519HDPublicKey.fromBase58(associatedSenderAccount.pubkey),
    #   destination: Ed25519HDPublicKey.fromBase58(associatedRecipientAccount.pubkey),
    #   owner: from.publicKey,
    #   amount: getRawQuantity(1.0, 5).toInt(),
    #   signers: signersPublic,
    # );

    # final message = Message(
    #   instructions: [
    #     instruction,
    #   ],
    # );

    # var recentBlockHash = await solanaClient.rpcClient.getRecentBlockhash();
    # int blockHeight = await solanaClient.rpcClient.getBlockHeight();

    # final CompiledMessage compiledMessage = message.compile(
    #   recentBlockhash: recentBlockHash.blockhash,
    #   feePayer: hopSignerPublicKey,
    # );

    # var tx = SignedTx(
    #   messageBytes: compiledMessage.data,
    #   signatures: [
    #     Signature(List.filled(64, 0), publicKey: hopSignerPublicKey),
    #     await from.sign(compiledMessage.data),
    #   ],
    # );

    # String _txe = tx.encode();

    alice = Keypair.from_bytes([205,213,7,246,167,206,37,209,161,129,168,160,90,103,198,142,83,177,214,203,80,29,71,245,56,152,15,8,235,174,62,79,138,198,145,111,119,33,15,237,89,201,122,89,48,221,224,71,81,128,45,97,191,105,37,228,243,238,130,151,53,221,172,125])
    bob = 'BobQoPqWy5cpFioy1dMTYqNH9WpC39mkAEDJWXECoJ9y'
    source_token_account = get_associated_token_address(PublicKey('ALisrzsaVqciCxy8r6g7MUrPoRo3CpGxPhwBbZzqZ9bA'), PublicKey(mint_public_key))
    destination_token_account = get_associated_token_address(PublicKey(bob), PublicKey(mint_public_key))

    account_metas = [
        AccountMeta(
            PublicKey(mint_public_key).to_solders(),
            True,
            True
        ),
        AccountMeta(
            source_token_account.to_solders(),
            True,
            True
        ),
        AccountMeta(
            destination_token_account.to_solders(),
            False,
            True
        ),
    ]
    data: bytes = SYSTEM_INSTRUCTIONS_LAYOUT.build(
        dict(
            type=InstructionType.TRANSFER,
            args=dict(lamports=5)
        )
    )
    instruction = Instruction(
        program_id=Pubkey(bytes(SYSTEM_PROGRAM_ID)),
        data=data,
        accounts=account_metas
    )

    message = Message([instruction], alice.pubkey())

    fee_payer = NullSigner(PublicKey(mint_public_key).to_solders())

    signature = alice.sign_message(bytes(1))

    tx = Transaction([fee_payer, alice], message, Hash.from_string(recent_blockhash))

    # tx.partial_sign(alice)

    return bytes(tx)