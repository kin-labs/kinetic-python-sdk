from kinetic_sdk.models.keypair import Keypair


def test_keypair_from_mnemonic():
    """ Test recovering a Keypair from mnemonic """
    TEST_MNEMONIC_PUBLIC_KEY = "5ZWj7a1f8tWkjBESHKgrLmXshuXxqeY9SYcfbshpAqPG"
    TEST_MNEMONIC_12 = 'pill tomorrow foster begin walnut borrow virtual kick shift mutual shoe scatter'
    keypair = Keypair.from_mnemonic(TEST_MNEMONIC_12)
    assert str(keypair.public_key) == TEST_MNEMONIC_PUBLIC_KEY


def test_keypair_generate_mnemonic():
    """ Test generating a mnemonic """
    mnemonic = Keypair.generate_mnemonic()
    print(mnemonic)


def test_get_keypair_mnemonic():
    """ Test generating a mnemonic """
    keypair = Keypair()
    print(keypair.mnemonic)


def test_keypair_creation():
    """ Test creating a Keypair """
    keypair = Keypair()
    mnemonic = Keypair.generate_mnemonic()
    print('mnemonic: ', mnemonic)

    keypair = Keypair.from_mnemonic(mnemonic)
    print('keypair: ', keypair)

    commitment = Commitment('Finalized')
    print('commitment: ', commitment)

    account = sdk.create_account(
        owner=keypair, commitment=commitment)
    print('account: ', account)

