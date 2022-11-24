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

# Kinetic Python SDK

Kinetic Python SDK is the official [python](https://www.python.org/) SDK for [Kinetic](https://github.com/kin-labs/kinetic) based on the [Kinetic SDK Standard](https://github.com/kin-labs/kinetic/discussions/317).

This SDK allows developers to rapidly integrate Kin and other SPL tokens in their app.

## Usage

In order to use this SDK, please head over to the [Kinetic Pyrhon SDK](https://developer.kin.org/docs/developers/python) documentation.

## Version

This SDK is built to work with `@kinetic/api@v1.0.0-rc.8`. Using it with other versions may lead to issues.

## Contributing

If you want to contribute to this SDK, please follow the steps below to get it running locally:

#### 1. Install the Poetry CLI on your local machine by visiting the link below:
[Install Poetry](https://python-poetry.org/docs/#installation)

#### 2. Install the OpenAPI Generator via NPM (for alternative installs visit: https://openapi-generator.tech)
`$ npm install @openapitools/openapi-generator-cli -g`

#### 3. Fetch the Kinetic Python repo
`$ git clone https://github.com/kin-labs/kinetic-python-sdk`

#### 4. Change into kinetic-python-sdk working directory
`$ cd kinetic-python-sdk`

#### 5. Run the tests
`$ make test`

#### 6. Generate OpenAPI Python client
`$ make generate`

## Directory labels
- [generated](https://github.com/kin-labs/kinetic-python-sdk/tree/main/src/kinetic_sdk/generated) Contains all the generated Python client code based on the openapi spec.
- [helpers](https://github.com/kin-labs/kinetic-python-sdk/tree/main/src/kinetic_sdk/helpers) Contains helper functions that simply calling the createAccount and makeTranfer sdk functions
- [models](https://github.com/kin-labs/kinetic-python-sdk/tree/main/src/kinetic_sdk/models) Here you can find all reference to classes to-be created and what they override.

## Contributing
To start contributing, take a look at the standard as this lays down the base for all clients.
This standard is subject to change so always review this before committing any meaningful work.
You can visit the standard [here](https://github.com/kin-labs/kinetic/discussions/317)

## Troubleshooting

If you have issues with [coincurve](https://github.com/ofek/coincurve) dependency in Apple Silicon M1 run this:
```
xcode-select --install
brew install autoconf automake libffi libtool pkg-config python
```
