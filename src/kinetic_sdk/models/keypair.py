from solana.keypair import Keypair as SolanaKeypair
from solders.keypair import Keypair as SoldersKeypair


class Keypair(object):

    keypair: SolanaKeypair = None


    def __init__(self):
        self.keypair = SolanaKeypair()
        return self.keypair        


    @staticmethod
    def from_mnemonic(mnemonic: str):
        pass


    @staticmethod
    def from_byte_array(key):
        return SolanaKeypair.from_secret_key(key)


    @staticmethod
    def from_secret_key(key):
        return SolanaKeypair.from_secret_key(key)


    @staticmethod
    def random():
        return SolanaKeypair()
    

    @staticmethod
    def from_solders(self, keypair: SoldersKeypair):
        return SolanaKeypair.from_solders(keypair)


    @staticmethod
    def to_solders(self):
        return self.keypair.to_solders()
