from solana.keypair import Keypair as SolanaKeypair
from solders.keypair import Keypair as SoldersKeypair
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip39WordsNum, Bip39Languages, Bip44, Bip44Coins, Bip44Changes
from bip_utils.utils.mnemonic import Mnemonic
from typing import Union

class Keypair(object):

    keypair: SolanaKeypair
    mnemonic: Mnemonic


    def __init__(self):
        self.mnemonic = Keypair.generate_mnemonic()
        self.keypair = SolanaKeypair.from_solders(Keypair.from_mnemonic(str(self.mnemonic)))


    @staticmethod
    def generate_mnemonic(strength: int = 128):
        if strength == 128:
            return Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_12)
        elif strength == 256:
            return Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24)


    @staticmethod
    def from_mnemonic(mnemonic_phrase: Union[str, Mnemonic]):
        return Keypair.from_mnemonic_set(str(mnemonic_phrase))[0]


    @staticmethod
    def from_mnemonic_set(mnemonic_phrase: Union[str, Mnemonic], fr = 0, to = 2):
        keypairs = [i for i in range(to)]
        seed_bytes = Bip39SeedGenerator(str(mnemonic_phrase), Bip39Languages.ENGLISH).Generate("")
        bip44_seeds = Bip44.FromSeed(seed_bytes, Bip44Coins.SOLANA).Purpose().Coin()
        for i in range(fr, to):
            soldersKeypair = SoldersKeypair.from_seed(bip44_seeds.Account(i).Change(Bip44Changes.CHAIN_EXT).PrivateKey().Raw().ToBytes())
            keypairs[i] = SolanaKeypair.from_solders(soldersKeypair)

        return keypairs


    @staticmethod
    def from_byte_array(key):
        if (type(key) is str):
            return SolanaKeypair.from_secret_key(Keypair.to_bytes_array(key))
        SolanaKeypair.from_secret_key(key)


    @staticmethod
    def from_secret_key(key):
        return SolanaKeypair.from_secret_key(key)


    @staticmethod
    def random():
        return SolanaKeypair()

    @staticmethod
    def from_secret(secret):
        keypair: SolanaKeypair = None
        if(Keypair.is_mnemonic(secret)):
            keypair = Keypair.from_mnemonic(secret)
        elif(Keypair.is_byte_array(secret)):
            keypair = Keypair.from_byte_array(secret)
        else:
            keypair = SolanaKeypair.from_secret_key(secret)

        if(keypair is None):
            raise Exception("Invalid secret")

        return keypair

    @staticmethod
    def is_mnemonic(secret):
        return len(secret.split(" ")) in [12, 24]


    @staticmethod
    def is_byte_array(secret):
        return secret.startswith("[") and secret.endswith("]")


    @staticmethod
    def from_solders(keypair: SoldersKeypair):
        return SolanaKeypair.from_solders(keypair)


    def to_solders(self):
        return self.keypair.to_solders()

    def to_bytes_array(secret):
        secret = secret.replace("[", "").replace("]", "").split(", ")
        return [eval(i) for i in secret]
