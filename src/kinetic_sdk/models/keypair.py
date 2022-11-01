from solana.keypair import Keypair as SolanaKeypair
from solders.keypair import Keypair as SoldersKeypair
from pybip39 import Mnemonic, Seed, Language

        

class Keypair(object):

    keypair: SolanaKeypair
    mnemonic: Mnemonic


    def __init__(self):
        self.keypair = SolanaKeypair()
        self.mnemonic = Keypair.generate_mnemonic()
        self.keypair = SolanaKeypair.from_solders(Keypair.from_mnemonic(str(self.mnemonic)))

    @staticmethod
    def generate_mnemonic():
        return Mnemonic()

    @staticmethod
    def from_mnemonic(mnemonic: str):
        mnemonic = Mnemonic.from_phrase(mnemonic, Language.English)
        passphrase = ""
        seed = Seed(mnemonic, passphrase)
        keypair = SoldersKeypair.from_seed_phrase_and_passphrase(mnemonic.phrase, passphrase)
        return keypair


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
