# flake8: noqa: E501
# pylint: disable=line-too-long,missing-module-docstring
from kinetic_sdk.keypair import Keypair

# fmt: off
ALICE_KEY = [205, 213, 7, 246, 167, 206, 37, 209, 161, 129, 168, 160, 90, 103, 198, 142, 83, 177, 214, 203, 80, 29, 71, 245, 56, 152, 15, 8, 235, 174, 62, 79, 138, 198, 145, 111, 119, 33, 15, 237, 89, 201, 122, 89, 48, 221, 224, 71, 81, 128, 45, 97, 191, 105, 37, 228, 243, 238, 130, 151, 53, 221, 172, 125]
# fmt: on

ALICE_KEYPAIR = Keypair.from_byte_array(ALICE_KEY)
ALICE_ACCOUNT = "ALisrzsaVqciCxy8r6g7MUrPoRo3CpGxPhwBbZzqZ9bA"
ALICE_TOKEN_ACCOUNT = "Ebq6K7xVh6PYQ8DrTQnD9fC91uQiyBMPGSV6JCG6GPdD"

BOB_ACCOUNT = "BobQoPqWy5cpFioy1dMTYqNH9WpC39mkAEDJWXECoJ9y"
BOB_TOKEN_ACCOUNT = "92gcR7aBdZDGvoC1cCSTSzQDediBZecy32B43mJtuUXT"
CHARLIE_ACCOUNT = "CharYfTvJSiH6LtDpkGUiVVZmeCn5Cenu2TzdJSbDJnG"

DEFAULT_MINT = "MoGaMuJnB3k8zXjBYBnHxHG47vWcW3nyb7bFYvdVzek"
FEE_PAYER = "oWNEYV3aMze3CppdgyFAiEj9xUJXkn85es1KscRHt8m"

TEST_MNEMONIC_12 = "pill tomorrow foster begin walnut borrow virtual kick shift mutual shoe scatter"
TEST_MNEMONIC_12_PUBLIC_KEY = "5F86TNSTre3CYwZd1wELsGQGhqG2HkN3d8zxhbyBSnzm"

TEST_MNEMONIC_12_KEYPAIR = {
    "mnemonic": TEST_MNEMONIC_12,
    "public_key": TEST_MNEMONIC_12_PUBLIC_KEY,
    "secret_key": "cWNhG6WhR4q6X5v8d65x6UgVR4buQJFkpKVvKiFDbbbZnoxpTJZLoCkCLZXpCYKc1QgyXYbhQpACYN8VKgS5xxq",
}


TEST_MNEMONIC_24 = "grab amused tattoo cruise industry corn welcome wealth tilt erupt gauge ankle remove toast journey heavy unit vibrant zoo blood notice jealous gesture cargo"
TEST_MNEMONIC_24_KEYPAIR = {
    "mnemonic": TEST_MNEMONIC_24,
    "public_key": "6pFBagvvyvBHuCkbMAiPTLn42nnHXrHC2zwWSdZ1NtVn",
    "secret_key": "WTqijcBccatWsAA6WJzaqgNzJVdARiBHceL5DQG15RbZCNn9jeoEjwMyKRiQqsPvLKGhgkQMoUgo2ybbZmStU3r",
}
