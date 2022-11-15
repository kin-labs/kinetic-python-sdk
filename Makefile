install:
	poetry install

test:
	poetry run pytest -s ./tests/

generate:
	rm -r src/kinetic_sdk/generated && openapi-generator-cli generate -i https://raw.githubusercontent.com/kin-labs/kinetic/main/api-swagger.json -g python -o src/kinetic_sdk/generated --additional-properties=packageName=client --global-property=modelTests=false,apiTests=false,modelDocs=false,apiDocs=false
	find . -name '*.py' -print -exec sed -i.bak 's/from client/from kinetic_sdk.generated.client/g' {} \;
	find . -name '*.bak' -print -exec rm {} \;

build:
	poetry build
