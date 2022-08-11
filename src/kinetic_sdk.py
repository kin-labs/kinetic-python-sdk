from kinetic_sdk_internal import KineticSdkInternal
from solana.keypair import Keypair

class KineticSdk(object):

    def __init__(self, environment, index):
        self.config = {}
        self.config['environment'] = environment
        self.config['index'] = index
        self.internal = KineticSdkInternal(self.config)

    def get_balance(self, account: str):
        return self.internal.get_balance(account)

    def get_history(self, account: str, mint: str):
        return self.internal.get_history(account, mint)

    def get_token_accounts(self, account: str, mint: str):
        return self.internal.get_token_accounts(account, mint)

    def create_account(self, owner: Keypair, mint: str):
        return self.internal.create_account(owner, mint)

    def make_transfer(self, owner: Keypair, destination: str, amount: int, mint: str, type):
        return self.internal.make_transfer(owner, destination, amount, mint, type)

    def init(self):
        config = self.internal.get_app_config(self.config['environment'], self.config['index'])
        self.config['mint'] = config['mint']['publicKey']

    @staticmethod
    def setup(environment, index):
        sdk = KineticSdk(environment, index)
        sdk.init()
        return sdk
