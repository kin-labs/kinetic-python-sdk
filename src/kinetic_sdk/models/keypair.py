from solana.keypair import Keypair as SolanaKeypair
from solders.keypair import Keypair as SoldersKeypair
from pybip39 import Mnemonic, MnemonicType, Language
from kinetic_bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes, Bip39Languages
from typing import Union

class Keypair(object):

    keypair: SolanaKeypair
    mnemonic: Mnemonic


    def __init__(self):
        self.keypair = SolanaKeypair()
        self.mnemonic = Keypair.generate_mnemonic()
        self.keypair = SolanaKeypair.from_solders(Keypair.from_mnemonic(str(self.mnemonic)))

    @staticmethod
    def generate_mnemonic(strength: int = 128):
        if strength == 128:
            return Mnemonic()
        elif strength == 256:
            return Mnemonic(MnemonicType.Words24)

    @staticmethod
    def from_mnemonic(mnemonic_phrase: Union[str, Mnemonic]):
        mnemonic = Mnemonic.from_phrase(str(mnemonic_phrase), Language.English)
        keypair = SoldersKeypair.from_seed_phrase_and_passphrase(mnemonic.phrase, "")
        return SolanaKeypair.from_solders(keypair)


    # FIXME: Remove this method, move the logic to from_mnemonic and make sure test do don't break.
    @staticmethod
    def from_mnemonic_standard_derivation_path(mnemonic_phrase: Union[str, Mnemonic]):
        seed_bytes = Bip39SeedGenerator(mnemonic_phrase, Bip39Languages.ENGLISH).Generate("")
        bip44_seed = Bip44.FromSeed(seed_bytes, Bip44Coins.SOLANA).Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).PrivateKey().Raw().ToBytes()
        keypair = SoldersKeypair.from_seed(bip44_seed)
        return SolanaKeypair.from_solders(keypair)


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
