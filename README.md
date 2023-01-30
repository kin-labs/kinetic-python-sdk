# Kinetic Python SDK

Kinetic Python SDK is the official [python](https://www.python.org/) SDK for [Kinetic](https://github.com/kin-labs/kinetic) based on the [Kinetic SDK Standard](https://github.com/kin-labs/kinetic/discussions/317).

This SDK allows developers to rapidly integrate Kin and other SPL tokens in their app.

## Usage

In order to use this SDK, please head over to the [Kinetic Pyrhon SDK](https://developer.kin.org/docs/developers/python) documentation.

## Version

This SDK is built to work with `@kinetic/api@v1.0.0-rc.16`. Using it with other versions may lead to issues.

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
