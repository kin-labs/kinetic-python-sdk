# pylint: disable=missing-class-docstring,missing-function-docstring,missing-module-docstring,import-error
from typing import Optional

from bip_utils import (
    Bip39Languages,
    Bip39MnemonicGenerator,
    Bip39SeedGenerator,
    Bip39WordsNum,
    Bip44,
    Bip44Changes,
    Bip44Coins,
)
from solana.keypair import Keypair as SolanaKeypair
from solana.publickey import PublicKey
from solders.keypair import Keypair as SoldersKeypair

from kinetic_sdk.helpers import base58_decode, base58_encode


class KineticKeypair:
    solana_keypair: SolanaKeypair

    mnemonic: Optional[str] = None
    public_key: str
    secret_key: str

    def __init__(self, secret_key: str):
        print("__init__: secret_key", secret_key)
        self.solana_keypair = SolanaKeypair.from_secret_key(base58_decode(secret_key))
        self.public_key = str(self.solana_keypair.public_key)
        print("__init__: public_key", self.public_key)
        self.secret_key = base58_encode(self.solana_keypair.secret_key)
        print("__init__: secret_key", self.secret_key)

    @property
    def solana(self) -> SolanaKeypair:
        return self.solana_keypair

    @property
    def solana_public_key(self) -> PublicKey:
        return self.solana_keypair.public_key

    @property
    def solana_secret_key(self) -> bytes:
        return self.solana_keypair.secret_key

    @staticmethod
    def from_byte_array(byte_array: list[int]) -> "KineticKeypair":
        data = bytes()
        for item in byte_array:
            data += bytes([item])

        return KineticKeypair.from_secret_key(secret_key=base58_encode(data))

    @staticmethod
    def from_mnemonic(mnemonic: str) -> "KineticKeypair":
        return KineticKeypair.from_mnemonic_set(mnemonic=mnemonic)[0]

    @staticmethod
    def from_mnemonic_set(mnemonic: str, from_index=0, to_index=1) -> list["KineticKeypair"]:
        # Always start with zero as minimum
        from_index = max(from_index, 0)
        # Always generate at least 1
        if to_index <= from_index:
            to_index = from_index + 1

        keypairs = list(range(from_index, to_index))

        seed = Bip39SeedGenerator(mnemonic, Bip39Languages.ENGLISH).Generate("")
        bip44_seeds = Bip44.FromSeed(seed, Bip44Coins.SOLANA).Purpose().Coin()

        for i in range(from_index, to_index):
            solders_keypair = SoldersKeypair.from_seed(
                bip44_seeds.Account(i).Change(Bip44Changes.CHAIN_EXT).PrivateKey().Raw().ToBytes()
            )
            kp = KineticKeypair.from_secret_key(secret_key=base58_encode(solders_keypair.secret()))
            kp.mnemonic = mnemonic
            keypairs[i] = kp

        return keypairs

    @staticmethod
    def from_secret(secret: str) -> 'KineticKeypair':
        # trim spaces and newlines from the secret
        secret = secret.strip()
        keypair: KineticKeypair
        if KineticKeypair._is_mnemonic(secret):
            keypair = KineticKeypair.from_mnemonic(mnemonic=secret)
        elif KineticKeypair._is_byte_array(secret):
            keypair = KineticKeypair._parse_byte_array(secret=secret)
        else:
            keypair = KineticKeypair.from_secret_key(secret_key=secret)

        if keypair is None:
            raise ValueError("Invalid secret")

        return keypair


    @staticmethod
    def from_secret_key(secret_key: str) -> "KineticKeypair":
        return KineticKeypair(secret_key)

    @staticmethod
    def generate_mnemonic(strength: 128 | 256 = 128) -> str:
        if strength not in [128, 256]:
            raise ValueError("Strength must be 128 or 256")
        words = Bip39WordsNum.WORDS_NUM_12 if strength == 128 else Bip39WordsNum.WORDS_NUM_24

        return str(Bip39MnemonicGenerator().FromWordsNumber(words))

    @staticmethod
    def random() -> 'KineticKeypair':
        mnemonic: str = KineticKeypair.generate_mnemonic()
        return KineticKeypair.from_mnemonic(mnemonic)

    @staticmethod
    def _parse_byte_array(secret: str) -> "KineticKeypair":
        secret = secret.replace('[', '').replace(']', '')
        byte_array: list[int] = []
        for item in secret.split(','):
            byte_array.append(int(item.strip()))
        return KineticKeypair.from_byte_array(byte_array=byte_array)

    @staticmethod
    def _is_byte_array(secret: str) -> bool:
        return str(secret).startswith("[") and secret.endswith("]")

    @staticmethod
    def _is_mnemonic(secret: str) -> bool:
        return len(str(secret).split(" ")) in [12, 24]



