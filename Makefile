install:
	poetry install

test:
	poetry run pytest -s ./tests/

generate:
	rm -r src/generated && openapi-generator-cli generate -i https://raw.githubusercontent.com/kin-labs/kinetic/dev/api-swagger.json -g python -o src/generated --additional-properties=packageName=kinetic_sdk_generated

build:
	poetry build
