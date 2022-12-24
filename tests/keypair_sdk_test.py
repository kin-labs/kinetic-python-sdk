from kinetic_sdk import Keypair, KineticSdk

sdk = KineticSdk.setup(
    endpoint='http://localhost:3000',
    environment='local',
    index=1
)

TEST_MNEMONIC_12 = 'pill tomorrow foster begin walnut borrow virtual kick shift mutual shoe scatter'
TEST_MNEMONIC_12_KEYPAIR = {
  'mnemonic': TEST_MNEMONIC_12,
  'public_key': '5F86TNSTre3CYwZd1wELsGQGhqG2HkN3d8zxhbyBSnzm',
  'secret_key': 'cWNhG6WhR4q6X5v8d65x6UgVR4buQJFkpKVvKiFDbbbZnoxpTJZLoCkCLZXpCYKc1QgyXYbhQpACYN8VKgS5xxq',
}


TEST_MNEMONIC_24 = 'grab amused tattoo cruise industry corn welcome wealth tilt erupt gauge ankle remove toast journey heavy unit vibrant zoo blood notice jealous gesture cargo'
TEST_MNEMONIC_24_KEYPAIR = {
  'mnemonic': TEST_MNEMONIC_24,
  'public_key': '6pFBagvvyvBHuCkbMAiPTLn42nnHXrHC2zwWSdZ1NtVn',
  'secret_key': 'WTqijcBccatWsAA6WJzaqgNzJVdARiBHceL5DQG15RbZCNn9jeoEjwMyKRiQqsPvLKGhgkQMoUgo2ybbZmStU3r',
}


def test_keypair_from_mnemonic():
    """ Test recovering a Keypair from mnemonic """
    keypair = Keypair.from_mnemonic(TEST_MNEMONIC_12)
    assert keypair.mnemonic == TEST_MNEMONIC_12
    assert str(keypair.public_key) == TEST_MNEMONIC_12_KEYPAIR['public_key']

    keypair = Keypair.from_mnemonic(TEST_MNEMONIC_24)
    assert keypair.mnemonic == TEST_MNEMONIC_24
    assert str(keypair.public_key) == TEST_MNEMONIC_24_KEYPAIR['public_key']


def test_keypair_generate_mnemonic():
    """ Test generating a mnemonic """
    mnemonic = Keypair.generate_mnemonic()
    # print('12-words', mnemonic)


def test_keypair_generate_mnemonic_24_words():
    """ Test generating a 24-word mnemonic """
    mnemonic = Keypair.generate_mnemonic(strength=256)
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
    """ Test mnemonic derivation path """
    TEST_MNEMONIC_12 = 'field pool drill reward habit engine useless mind hybrid tiny lamp key'
    TEST_MNEMONIC_PUBLIC_KEY = '9Qrp2PXZSBuWf7CoFd2TMYS4ohUBt12p8rD8wF2W2owD'
    keypair = Keypair.from_mnemonic(TEST_MNEMONIC_12)
    kp_from_secret = Keypair.from_secret(TEST_MNEMONIC_12)
    assert str(keypair.public_key) == TEST_MNEMONIC_PUBLIC_KEY
    assert kp_from_secret.secret_key == keypair.secret_key
    assert kp_from_secret.public_key == keypair.public_key


def test_keypair_from_secret():
    """ Test recovering a Keypair from secret """
    solanaKeypair = Keypair()
    kp1 = solanaKeypair.keypair._solders

    from_byte_array = Keypair.from_secret(f"{kp1.to_solders().to_bytes_array()}")
    assert from_byte_array.secret_key == kp1.secret_key
    assert from_byte_array.public_key == kp1.public_key

    from_mnemonic = Keypair.from_secret(solanaKeypair.mnemonic)
    assert from_mnemonic.secret_key == kp1.secret_key
    assert from_mnemonic.public_key == kp1.public_key
    assert from_mnemonic.mnemonic == solanaKeypair.mnemonic

    from_secret_key = Keypair.from_secret(kp1.secret_key)
    assert from_secret_key.secret_key == kp1.secret_key
    assert from_secret_key.public_key == kp1.public_key
