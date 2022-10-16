from kinetic_sdk_internal import KineticSdkInternal

from solana.keypair import Keypair

from models.transaction_type import TransactionType
from models.public_key_string import PublicKeyString


class KineticSdk(object):

    def __init__(self, environment, index):
        self.config = {'environment': environment, 'index': index}
        self.internal = KineticSdkInternal(self.config)

    def get_balance(self, account: PublicKeyString):
        return self.internal.get_balance(account)

    def get_history(self, account: PublicKeyString, mint: PublicKeyString):
        return self.internal.get_history(account, mint)

    def get_token_accounts(self, account: PublicKeyString, mint: PublicKeyString):
        return self.internal.get_token_accounts(account, mint)

    def create_account(self, owner: Keypair, mint: PublicKeyString):
        return self.internal.create_account(owner, mint)

    def make_transfer(self, owner: Keypair, destination: PublicKeyString, amount: int, mint: PublicKeyString,
                      tx_type: TransactionType):
        return self.internal.make_transfer(owner, destination, amount, mint, tx_type)

    def request_airdrop(self, account: PublicKeyString, amount: str, mint: PublicKeyString, commitment='Confirmed'):
        return self.internal.request_airdrop(account, amount, mint, commitment)

    def init(self):
        config = self.internal.get_app_config(self.config['environment'], self.config['index'])
        self.config['mint'] = config['mint']['public_key']

    @staticmethod
    def setup(environment, index):
        sdk = KineticSdk(environment, index)
        sdk.init()
        return sdk
