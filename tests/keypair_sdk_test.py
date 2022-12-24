# flake8: noqa: E501
# pylint: disable=missing-function-docstring,missing-module-docstring,line-too-long,fixme
from kinetic_sdk import Keypair, KineticSdk
from tests.fixtures import (
    TEST_MNEMONIC_12,
    TEST_MNEMONIC_12_KEYPAIR,
    TEST_MNEMONIC_12_PUBLIC_KEY,
    TEST_MNEMONIC_24,
    TEST_MNEMONIC_24_KEYPAIR,
)

sdk = KineticSdk.setup(endpoint="http://localhost:3000", environment="local", index=1)


def test_keypair_from_mnemonic():
    """Test recovering a Keypair from mnemonic"""
    keypair = Keypair.from_mnemonic(TEST_MNEMONIC_12)
    assert keypair.mnemonic == TEST_MNEMONIC_12
    assert str(keypair.public_key) == TEST_MNEMONIC_12_KEYPAIR["public_key"]

    keypair = Keypair.from_mnemonic(TEST_MNEMONIC_24)
    assert keypair.mnemonic == TEST_MNEMONIC_24
    assert str(keypair.public_key) == TEST_MNEMONIC_24_KEYPAIR["public_key"]


def test_keypair_generate_mnemonic():
    """Test generating a mnemonic"""
    mnemonic = Keypair.generate_mnemonic()
    # FIXME: Implement asserts
    print("12-words", mnemonic)


def test_keypair_generate_mnemonic_24_words():
    """Test generating a 24-word mnemonic"""
    mnemonic = Keypair.generate_mnemonic(strength=256)
    # FIXME: Implement asserts
    print("24-words", mnemonic)


def test_get_keypair_mnemonic():
    """Test generating a mnemonic"""
    keypair = Keypair()
    # FIXME: Implement asserts
    print(keypair.mnemonic)


def test_keypair_creation():
    """Test creating a Keypair"""
    # keypair = Keypair()
    mnemonic = Keypair.generate_mnemonic()
    keypair = Keypair.from_mnemonic(mnemonic)
    account = sdk.create_account(owner=keypair)
    # FIXME: Implement asserts
    print("account: ", account)


def test_mnemonic_derivation_path():
    """Test mnemonic derivation path"""
    keypair = Keypair.from_mnemonic(TEST_MNEMONIC_12)
    kp_from_secret = Keypair.from_secret(TEST_MNEMONIC_12)
    assert str(keypair.public_key) == TEST_MNEMONIC_12_PUBLIC_KEY
    assert kp_from_secret.secret_key == keypair.secret_key
    assert kp_from_secret.public_key == keypair.public_key


def test_keypair_from_secret():
    """Test recovering a Keypair from secret"""
    solana_keypair = Keypair()
    # pylint: disable=protected-access
    kp1 = solana_keypair.keypair._solders

    from_byte_array = Keypair.from_secret(f"{kp1.to_solders().to_bytes_array()}")
    assert from_byte_array.secret_key == kp1.secret_key
    assert from_byte_array.public_key == kp1.public_key

    from_mnemonic = Keypair.from_secret(solana_keypair.mnemonic)
    assert from_mnemonic.secret_key == kp1.secret_key
    assert from_mnemonic.public_key == kp1.public_key
    assert from_mnemonic.mnemonic == solana_keypair.mnemonic

    from_secret_key = Keypair.from_secret(kp1.secret_key)
    assert from_secret_key.secret_key == kp1.secret_key
    assert from_secret_key.public_key == kp1.public_key
