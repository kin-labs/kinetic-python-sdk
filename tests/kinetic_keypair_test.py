# flake8: noqa: E501
# pylint: disable=missing-function-docstring,missing-module-docstring,line-too-long,fixme

from kinetic_sdk.kinetic_keypair import KineticKeypair
from tests.fixtures import (
    TEST_MNEMONIC_12,
    TEST_MNEMONIC_12_KEYPAIR,
    TEST_MNEMONIC_12_SET,
    TEST_MNEMONIC_24,
    TEST_MNEMONIC_24_KEYPAIR,
    TEST_PUBLIC_KEY,
    TEST_SECRET_BYTEARRAY,
    TEST_SECRET_KEY, TEST_MNEMONIC_24_SET,
)


def test_should_generate_a_keypair():
    """should generate a KeyPair"""
    kp = KineticKeypair.random()
    assert isinstance(kp, KineticKeypair)

    assert kp.mnemonic is not None
    assert kp.secret_key is not None
    assert kp.public_key is not None


def test_should_return_generate_a_keypair_from_mnemonic():
    """should return generate a KeyPair from mnemonic"""
    kp = KineticKeypair.random()
    restored = KineticKeypair.from_mnemonic(kp.mnemonic)
    assert restored.mnemonic ==  kp.mnemonic
    assert restored.secret_key ==  kp.secret_key
    assert restored.public_key ==  kp.public_key


def test_should_generate_a_mnemonic_phrase_12_chars():
    """should generate a Mnemonic phrase (12 chars)"""
    mnemonic = KineticKeypair.generate_mnemonic()

    assert isinstance(mnemonic, str)
    assert len(mnemonic.split(" ")) == 12


def test_should_generate_a_mnemonic_phrase_24_chars():
    """should generate a Mnemonic phrase (24 chars)"""
    mnemonic = KineticKeypair.generate_mnemonic(strength=256)

    assert isinstance(mnemonic, str)
    assert len(mnemonic.split(" ")) == 24


def test_should_create_and_import_keypair_from_secret_byte_array_mnemonic_secret_key():
    """should create and import keypair fromSecret (byte array, mnemonic, secret_key)"""
    pass


def test_should_create_and_import_keypair():
    """should create and import keypair"""
    kp1 = KineticKeypair.random()
    kp2 = KineticKeypair.from_secret_key(kp1.secret_key)
    kp_secret = KineticKeypair.from_secret(kp1.secret_key)

    assert  kp1.secret_key == kp2.secret_key
    assert  kp1.public_key == kp2.public_key
    assert  kp_secret.public_key == kp2.public_key


def test_should_import_from_a_bytearray():
    """should import from a bytearray"""
    kp = KineticKeypair.from_byte_array(byte_array=TEST_SECRET_BYTEARRAY)
    kp_secret = KineticKeypair.from_secret(secret=str(TEST_SECRET_BYTEARRAY))

    assert isinstance(kp, KineticKeypair)
    assert isinstance(kp_secret, KineticKeypair)
    assert isinstance(kp.secret_key, str)
    assert isinstance(kp.public_key, str)
    assert kp.public_key == TEST_PUBLIC_KEY
    assert kp_secret.public_key == TEST_PUBLIC_KEY
    assert kp.secret_key == TEST_SECRET_KEY
    assert kp_secret.secret_key == TEST_SECRET_KEY
    assert kp.mnemonic is None
    assert kp_secret.mnemonic is None


def test_should_import_and_existing_secret():
    """should import and existing secret"""
    kp = KineticKeypair.from_secret_key(secret_key=TEST_SECRET_KEY)

    assert isinstance(kp, KineticKeypair)
    assert isinstance(kp.secret_key, str)
    assert isinstance(kp.public_key, str)
    assert kp.public_key == TEST_PUBLIC_KEY
    assert kp.secret_key == TEST_SECRET_KEY
    assert kp.mnemonic is None


def test_should_import_a_mnemonic_12_chars_and_get_1_keypair():
    """should import a mnemonic (12 chars) and get 1 keypair"""
    kp = KineticKeypair.from_mnemonic(mnemonic=TEST_MNEMONIC_12)
    kp_secret = KineticKeypair.from_secret(secret=TEST_MNEMONIC_12)

    assert isinstance(kp, KineticKeypair)
    assert isinstance(kp_secret, KineticKeypair)

    assert kp.mnemonic == TEST_MNEMONIC_12_KEYPAIR["mnemonic"]
    assert kp_secret.mnemonic == TEST_MNEMONIC_12_KEYPAIR["mnemonic"]
    assert kp.public_key == TEST_MNEMONIC_12_KEYPAIR["public_key"]
    assert kp_secret.public_key == TEST_MNEMONIC_12_KEYPAIR["public_key"]
    assert kp.secret_key == TEST_MNEMONIC_12_KEYPAIR["secret_key"]
    assert kp_secret.secret_key == TEST_MNEMONIC_12_KEYPAIR["secret_key"]


def test_should_import_a_mnemonic_24_chars_and_get_1_keypair():
    """should import a mnemonic (24 chars) and get 1 keypair"""
    kp = KineticKeypair.from_mnemonic(mnemonic=TEST_MNEMONIC_24)
    kp_secret = KineticKeypair.from_secret(secret=TEST_MNEMONIC_24)

    assert isinstance(kp, KineticKeypair)
    assert isinstance(kp_secret, KineticKeypair)

    assert kp.mnemonic == TEST_MNEMONIC_24_KEYPAIR["mnemonic"]
    assert kp_secret.mnemonic == TEST_MNEMONIC_24_KEYPAIR["mnemonic"]
    assert kp.public_key == TEST_MNEMONIC_24_KEYPAIR["public_key"]
    assert kp_secret.public_key == TEST_MNEMONIC_24_KEYPAIR["public_key"]
    assert kp.secret_key == TEST_MNEMONIC_24_KEYPAIR["secret_key"]
    assert kp_secret.secret_key == TEST_MNEMONIC_24_KEYPAIR["secret_key"]


def test_should_import_multiple_from_a_mnemonic_12_chars():
    """should import multiple from a mnemonic (12 chars)"""
    kps: list[KineticKeypair] = KineticKeypair.from_mnemonic_set(mnemonic=TEST_MNEMONIC_12, from_index=0, to_index=10)

    assert isinstance(kps, list)
    assert len(kps) == 10

    for index, kp in enumerate(kps):
        current = TEST_MNEMONIC_12_SET[index]
        assert kp.public_key == current["public_key"]
        assert kp.secret_key == current["secret_key"]
        assert kp.mnemonic == current["mnemonic"]


def test_should_import_multiple_from_a_mnemonic_24_chars():
    """should import multiple from a mnemonic (24 chars)"""
    kps: list[KineticKeypair] = KineticKeypair.from_mnemonic_set(mnemonic=TEST_MNEMONIC_24, from_index=0, to_index=10)

    assert isinstance(kps, list)
    assert len(kps) == 10

    for index, kp in enumerate(kps):
        current = TEST_MNEMONIC_24_SET[index]
        assert kp.public_key == current["public_key"]
        assert kp.secret_key == current["secret_key"]
        assert kp.mnemonic == current["mnemonic"]


def test_should_throw_an_error_when_we_put_in_unexpected_values():
    """should throw an error when we put in unexpected values"""
    pass
