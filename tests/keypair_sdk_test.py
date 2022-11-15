from kinetic_sdk import KineticSdk
from kinetic_sdk.models.keypair import Keypair

sdk = KineticSdk.setup(
    endpoint='http://localhost:3000',
    environment='local',
    index=1
)


def test_keypair_from_mnemonic():
    """ Test recovering a Keypair from mnemonic """
    TEST_MNEMONIC_PUBLIC_KEY = "5ZWj7a1f8tWkjBESHKgrLmXshuXxqeY9SYcfbshpAqPG"
    TEST_MNEMONIC_12 = 'pill tomorrow foster begin walnut borrow virtual kick shift mutual shoe scatter'
    keypair = Keypair.from_mnemonic(TEST_MNEMONIC_12)
    assert str(keypair.public_key) == TEST_MNEMONIC_PUBLIC_KEY


def test_keypair_from_mnemonic_24_words():
    """ Test recovering a Keypair from mnemonic """
    TEST_MNEMONIC_24 = 'grab amused tattoo cruise industry corn welcome wealth tilt erupt gauge ankle remove toast journey heavy unit vibrant zoo blood notice jealous gesture cargo'
    TEST_MNEMONIC_24_PUBLIC_KEY = '36hssW7DqagnHyC3dPjD59kjiUnYWrYd8hXeQ3zZ5kUK'
    keypair = Keypair.from_mnemonic(TEST_MNEMONIC_24)
    assert str(keypair.public_key) == TEST_MNEMONIC_24_PUBLIC_KEY


def test_keypair_generate_mnemonic():
    """ Test generating a mnemonic """
    mnemonic = Keypair.generate_mnemonic()
    assert len(str(mnemonic).split()) == 12
    # print('12-words', mnemonic)


def test_keypair_generate_mnemonic_24_words():
    """ Test generating a 24-word mnemonic """
    mnemonic = Keypair.generate_mnemonic(strength=256)
    assert len(str(mnemonic).split()) == 24
    # print('24-words', mnemonic)


def test_get_keypair_mnemonic():
    """ Test generating a mnemonic """
    keypair = Keypair()
    # print(keypair.mnemonic)


def test_keypair_creation():
    """ Test creating a Keypair """
    keypair = Keypair()
    mnemonic = Keypair.generate_mnemonic()
    keypair = Keypair.from_mnemonic(mnemonic)
    account = sdk.create_account(owner=keypair)
    # print('account: ', account)


def test_mnemonic_derivation_path():
    """ Test standard derivation path mnemonics """
    keypair = Keypair.from_mnemonic('field pool drill reward habit engine useless mind hybrid tiny lamp key')
    # assert str(keypair.public_key) == '9Qrp2PXZSBuWf7CoFd2TMYS4ohUBt12p8rD8wF2W2owD'
    # print("public key: " + str(keypair.public_key))
