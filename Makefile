install:
	poetry install

test:
	poetry run pytest -s

generate:
	rm -r src/generated && openapi-generator-cli generate -i https://raw.githubusercontent.com/kin-labs/kinetic/dev/api-swagger.json -g python -o src/generated

dev_sdk:
	cd kinetic-sdk/kinetic_sdk && nodemon --exec python3 __main__.py

build:
	poetry build
