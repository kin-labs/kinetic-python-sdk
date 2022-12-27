# flake8: noqa: E501
# pylint: disable=line-too-long,missing-module-docstring
from kinetic_sdk.keypair import Keypair

TEST_SECRET_KEY = "4j3PbCCYvcAz1FbKGs7fBoQ5cd8piWCsQm5k6wNnTTzEtE6aM8JZ2AJaaJTjZJgGk9LywyonNHcVopHAwrMqh6kr"
TEST_PUBLIC_KEY = "5ZWj7a1f8tWkjBESHKgrLmXshuXxqeY9SYcfbshpAqPG"


# fmt: off
ALICE_KEY = [205, 213, 7, 246, 167, 206, 37, 209, 161, 129, 168, 160, 90, 103, 198, 142, 83, 177, 214, 203, 80, 29, 71, 245, 56, 152, 15, 8, 235, 174, 62, 79, 138, 198, 145, 111, 119, 33, 15, 237, 89, 201, 122, 89, 48, 221, 224, 71, 81, 128, 45, 97, 191, 105, 37, 228, 243, 238, 130, 151, 53, 221, 172, 125]
TEST_SECRET_BYTEARRAY = [186, 78, 68, 54, 63, 205, 1, 141, 2, 89, 45, 80, 77, 168, 215, 120, 56, 57, 72, 222, 50, 140, 31, 236, 254, 35, 208, 163, 138, 186, 225, 18, 67, 194, 241, 235, 28, 5, 209, 235, 248, 58, 150, 42, 218, 71, 43, 177, 183, 62, 55, 96, 216, 41, 59, 146, 121, 132, 223, 24, 39, 109, 3, 163]


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

TEST_MNEMONIC_12_SET = [
    TEST_MNEMONIC_12_KEYPAIR,
    {
        "mnemonic": TEST_MNEMONIC_12,
        "public_key": "AWjbG5SH5VEay5ksZbGHHgJhYRhM1rsN5Z538cfFvs4a",
        "secret_key": "CnJAJFfB8PkLPAGVfc7Pc9J2cWaCAiN65j44DFDP8ub7R1jN1XRkgT7FFBdBy9pUB33UmdAskuB5ZLPspH6U9jL",
    },
    {
        "mnemonic": TEST_MNEMONIC_12,
        "public_key": "TdFkuCzMB6ikLWbhxXkHT8ZZFdqD7LrD5QbuRYQCp18",
        "secret_key": "5ZKRCfEZpp5gchtkJTFJpPJQcbjR4M99L2mYRRcAWdXCE4Gfvd7CwdZgvDHcMeMTyGBLKiVEoqQ7etnGy3JnXtwc",
    },
    {
        "mnemonic": TEST_MNEMONIC_12,
        "public_key": "C7xHnBLteo5QZwc1Dzgu2aMvPVd5FwsX44cH6DMMszPz",
        "secret_key": "4mKLiQGyBvp9BGoF1FUtvLTLc2v9UormC6Aqva7eM2nTFnMUWj5KaTCSELUMyp4otJ253oZnJHApjUFV6CB7rQ7i",
    },
    {
        "mnemonic": TEST_MNEMONIC_12,
        "public_key": "7QJUf8m94wnSrukK7HQsbBZ2V4NVQQUuvZ5wdux9a5Lu",
        "secret_key": "4YudKZdE1MHpFJuXjKZGDERJ8Zh4e3wY3RmPw7csm3dmDTsd1iKtoyFuSYA6kmEzDTmLT8Dz68NUQNoe3jYQZexZ",
    },
    {
        "mnemonic": TEST_MNEMONIC_12,
        "public_key": "GkeNvLEAznNwPV47rXahTuYtqqCpzFs1g3gb2jq7x8Kd",
        "secret_key": "4MqYS4wyuxJsR48yvCy4jULnqAFxLscsUVW3eMoHzBPSNKyAX8rXtkEg3TQkgznN1G6iNfJHTf3mPhrvFh7bhyKR",
    },
    {
        "mnemonic": TEST_MNEMONIC_12,
        "public_key": "8T1j8WyQc726rByayWTz1tZZwMV2A6U1C4Ase2FxHgib",
        "secret_key": "Bb8z3xU7NmUxoX716NoZBUWXK8bciXJdZnknbgsUjaFm8S1zaFGipzYQTT2bf8x3xk79VjhP6KrfevwTEMZSZ6F",
    },
    {
        "mnemonic": TEST_MNEMONIC_12,
        "public_key": "CV2sNJvxqdHRQW2pejnGjLMqWXBy61jnx3uExxZ7n3CW",
        "secret_key": "5sJkm11xJgsztEHgPGNMRwVzBHwhJtf6kNaH9MBCwW6JiTe5aBDDy142JuM48rmbhuVVRmfgx9QDRYKbRRN9xvyp",
    },
    {
        "mnemonic": TEST_MNEMONIC_12,
        "public_key": "32e2ughnjjJ9MxuBb7JystX81Mh52qNfm8Kh9nMPXYtM",
        "secret_key": "5PwFc5bJ2cxMe8zeQRZzyL1Md3KAxh4pBVbv4Myo9m6HaPEnYvT7SDmYY8tuvXuHy1JZYN86L5pNnG9J6LfGxcLD",
    },
    {
        "mnemonic": TEST_MNEMONIC_12,
        "public_key": "36herGLdWaFZ9raFLeXBLE43t1oMwgd4yoUAAKaSTHKR",
        "secret_key": "ByHWNEnSCyoz3LzqnV9xRoKMKEWW9thGXEUp5XCP863ymhk7zhd54j8svVxgrKPDa9yboLbdobQMEuX7s4X4SsV",
    },
]

TEST_MNEMONIC_24_SET = [
    TEST_MNEMONIC_24_KEYPAIR,
    {
        "mnemonic": TEST_MNEMONIC_24,
        "public_key": "Foo948ttNuYa8SsfHX78BVyPVA7P7MsV8u43ZeQ1RBxm",
        "secret_key": "TcauP27RkmyhH2AsVaPh5rCofCN4xCoB1h5MgUT6eRoJ7GiVPDBqtW1dAmh9CNcHSqCVnoEFUbRhfApM6oLrUDF",
    },
    {
        "mnemonic": TEST_MNEMONIC_24,
        "public_key": "3ySWEh9mvVUpzMYYcqEv7VeAQp7ueGFAjUg1G9DBTjD5",
        "secret_key": "48wHgpEEb1f14kcYAyskTmUY9WnzLXuGUi1qmGiZr89uEmNo8g3uDNsk4aNjMaAfrE4oew7tk7VXWtUj8jWZGdbR",
    },
    {
        "mnemonic": TEST_MNEMONIC_24,
        "public_key": "HyMtaWzweBgpmgDf2dn8RhsM1c9m48VPQFjV6DAkHxbv",
        "secret_key": "46HfvZCsmSCnS9akRqULDci7313KQGk7Ndv7PXejTa4rnEtH7PnGMUo5jxkJwMJjifFxHyfJSkYcziEBqJqGPQYL",
    },
    {
        "mnemonic": TEST_MNEMONIC_24,
        "public_key": "5SZcAkce1YHt5D4ANfxQGBo1fRcjn7jbCaUGgaBPz8or",
        "secret_key": "3Gr9wYRLhz9LLhkSTYy1TsXyUbDcsfhVUxpDxDrHSjdY2J1tNBQWRZ4qdFvbH5AiMJCvq9qhxZc6j1RinPXMWDMa",
    },
    {
        "mnemonic": TEST_MNEMONIC_24,
        "public_key": "77VRnnzwRTeQLDpNDfMh8DrDkzbAtcuKncZyWN49oegG",
        "secret_key": "vrMzreRiV8Abz2WxqZhgh2Hmg5Mnc65QD3P1tr5Y7a296d7Y4FrUBppGCUAz2qCa6iNVUjygZu4SMiRDmW59Vbe",
    },
    {
        "mnemonic": TEST_MNEMONIC_24,
        "public_key": "GRwsvJC92A9UB4eEcpzuxPqsuBdKRjd731uGp6BLbPJv",
        "secret_key": "4ZPFuK3dS189sJFXdTiVRXeVA7ZV4LPgUUgXJwx7WVWMVCpafG3L1D2j1Z4dSJzamyYruHCSYWrwP6s8HhGLTYS2",
    },
    {
        "mnemonic": TEST_MNEMONIC_24,
        "public_key": "piCoBHqPoK4dhg84g1NajB6vdJX785G3wT2rExaQ6Q3",
        "secret_key": "3iUkSFmpVM4rZUsMJqGH1ajY3tWxG9A64agQwaPCZ1m5Yc3V8JacEPnAu3oDdhxTARHnpXKBBVcDJhv9cR2JDvd9",
    },
    {
        "mnemonic": TEST_MNEMONIC_24,
        "public_key": "6EeiyS9X6222PeUzpKA32jc3ZEkpTKms3qNZEmySm1DS",
        "secret_key": "8BJqbw31Zmn7887LtFtevmmGaUm5BNUvMB1tsnLdzCv5TFPTodYDCsKCFovHoL1BSZwGxbixDZoWwszLpSyYKXv",
    },
    {
        "mnemonic": TEST_MNEMONIC_24,
        "public_key": "DhW8bCabXWMJYg99rtZyy2XWax8J5wfLh8kmkpDxbR8G",
        "secret_key": "3P4zpjXuBtxH8hMguo8k68Nz3mDYRto3CaMkSm55TtPZzinRYg76uyvy2CBimcegBRThH92H9MzffYShJB62W8ya",
    },
]
