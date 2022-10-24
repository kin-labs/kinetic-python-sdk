from kinetic_sdk.kinetic_sdk_internal import KineticSdkInternal

from solana.keypair import Keypair

from models.transaction_type import TransactionType
from models.public_key_string import PublicKeyString


class KineticSdk(object):

    def __init__(self, endpoint, environment, index):
        self.config = {'endpoint': endpoint, 'environment': environment, 'index': index}
        self.internal = KineticSdkInternal(self.config)

    def create_account(self, owner: Keypair, mint: PublicKeyString):
        return self.internal.create_account(owner, mint)

    def get_balance(self, account: PublicKeyString):
        return self.internal.get_balance(account)

    def get_explorer_url(self, path: str):
        return self.internal.get_explorer_url(path)

    def get_history(self, account: PublicKeyString, mint: PublicKeyString):
        return self.internal.get_history(account, mint)

    def get_token_accounts(self, account: PublicKeyString, mint: PublicKeyString):
        return self.internal.get_token_accounts(account, mint)

    def get_transaction(self, signature: str):
        return self.internal.get_transaction(signature)

    def make_transfer(self, owner: Keypair, destination: PublicKeyString, amount: int, mint: PublicKeyString,
                      tx_type: TransactionType):
        return self.internal.make_transfer(owner, destination, amount, mint, tx_type)

    def make_transfer_batch(self):
        # Check TS one
        pass

    def request_airdrop(self, account: PublicKeyString, amount: str, mint: PublicKeyString, commitment='Confirmed'):
        return self.internal.request_airdrop(account, amount, mint, commitment)

    def init(self):
        # TODO: Set up Solana instance
        config = self.internal.get_app_config(self.config['environment'], self.config['index'])
        self.config['mint'] = config['mint']['public_key']

    @staticmethod
    def setup(endpoint, environment, index):
        sdk = KineticSdk(endpoint, environment, index)
        sdk.init()
        return sdk
