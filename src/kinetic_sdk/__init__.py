from typing import List, Dict
from kinetic_sdk.kinetic_sdk_internal import KineticSdkInternal

from kinetic_sdk.models.transaction_type import TransactionType
from kinetic_sdk.models.public_key_string import PublicKeyString
from kinetic_sdk.models.keypair import Keypair

from kinetic_sdk.generated.client.model.commitment import Commitment


class KineticSdk(object):

    def __init__(self, endpoint, environment, index, headers):
        self.config = { 'endpoint': endpoint, 'environment': environment, 'index': index, 'headers': headers }
        self.internal = KineticSdkInternal(self.config)

    def close_account(
        self,
        account: PublicKeyString,
        commitment=Commitment("Confirmed"),
        mint: PublicKeyString = None,
        reference_id: str = None,
        reference_type: str = None
    ):
        return self.internal.close_account(
            account,
            commitment,
            mint,
            reference_id,
            reference_type
        )

    def create_account(
        self,
        owner: Keypair,
        mint: PublicKeyString = None,
        commitment=Commitment("Confirmed"),
        reference_id: str = None,
        reference_type: str = None
    ):
        return self.internal.create_account(owner, mint, reference_id, reference_type, commitment)

    def get_account_info(self, account: PublicKeyString):
        return self.internal.get_account_info(account)

    def get_balance(self, account: PublicKeyString):
        return self.internal.get_balance(account)

    def get_explorer_url(self, path: str):
        return self.internal.get_explorer_url(path)

    def get_history(self, account: PublicKeyString, mint: PublicKeyString = None):
        return self.internal.get_history(account, mint)

    def get_token_accounts(self, account: PublicKeyString, mint: PublicKeyString = None):
        return self.internal.get_token_accounts(account, mint)

    def get_transaction(self, signature: str):
        return self.internal.get_transaction(signature)

    def make_transfer(
        self,
        owner: Keypair,
        destination: PublicKeyString,
        amount: str,
        tx_type: TransactionType = TransactionType.NONE,
        mint: PublicKeyString = None,
        commitment=Commitment("Confirmed"),
        reference_id: str = None,
        reference_type: str = None,
        sender_create: bool = False
    ):
        return self.internal.make_transfer(owner, destination, amount, mint, tx_type, reference_id, reference_type, sender_create, commitment)

    def make_transfer_batch(
        self,
        owner: Keypair,
        destinations: List[Dict[PublicKeyString, str]],
        tx_type: TransactionType = TransactionType.NONE,
        mint: PublicKeyString = None,
        commitment=Commitment("Confirmed"),
        reference_id: str = None,
        reference_type: str = None
    ):
        return self.internal.make_transfer_batch(owner, destinations, mint, tx_type, reference_id, reference_type, commitment)

    def request_airdrop(
        self,
        account: PublicKeyString,
        amount: str,
        mint: PublicKeyString = None,
        commitment=Commitment("Confirmed")
    ):
        return self.internal.request_airdrop(account, amount, mint, commitment)

    def init(self):
        # TODO: Set up Solana instance
        config = self.internal.get_app_config(self.config['environment'], self.config['index'])
        self.config['api'] = config['api']
        self.config['app'] = config['app']
        self.config['mint'] = config['mint']
        self.config['mints'] = config['mints']


    @staticmethod
    def setup(endpoint, environment, index, headers = None):
        sdk = KineticSdk(endpoint, environment, index, headers)
        sdk.init()
        return sdk

