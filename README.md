# kinetic-python

Python SDK implementation to use [Kinetic](https://kinetic.kin.org/) by [Kin Foundation](https://kin.org/)

## Installation

```
pip install kinetic-sdk
```

## Usage

### Initialization

```py
import kinetic_sdk

environment = 'devnet'
app_index = 1
sdk = kinetic_sdk.KineticSdk.setup(environment, app_index)
```

### Get Account History

```py
history = sdk.get_history(account_public_key, mint_public_key)
```

### Get Token Accounts

```py
token_accounts = sdk.get_token_accounts(account_public_key, mint_public_key)
```

### Request Airdrop

```py
airdrop = sdk.request_airdrop(account_public_key, amount_str, mint_public_key)
```

### Create Account

```py
owner = Keypair.generate()
account = sdk.create_account(owner, mint_public_key)
```

### Make Transfer

```py
tx = sdk.make_transfer(
    owner=alice_keypair,
    destination=bob_public_key, 
    amount=1, 
    mint=mint_public_key, 
    tx_type=TransactionType.NONE
)
```

# Documentation

This [file](https://github.com/kin-labs/kinetic-python/blob/main/src/__main__.py) can be followed for sample code, but more documentation and samples be [here](https://314-refactor-for-kinetic.kin-developer-docs.pages.dev/developers/python/).

# Development

Clone this request

```
git clone git@github.com:kin-labs/kinetic-python.git
```

Install the dependencies, the project uses [Poetry](https://python-poetry.org/), so you don't need to worry about creating virtual environments because it will create it for you.
```
make install
```

Run test

```
make test
```

