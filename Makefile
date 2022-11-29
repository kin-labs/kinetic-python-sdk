install:
	poetry install

test:
	poetry run pytest -s ./tests/

generate:
	rm -r src/kinetic_sdk/generated && openapi-generator-cli generate -i https://raw.githubusercontent.com/kin-labs/kinetic/main/api-swagger.json -g python -o src/kinetic_sdk/generated --additional-properties=packageName=client --global-property=modelTests=false,apiTests=false,modelDocs=false,apiDocs=false
	find src/kinetic_sdk/generated -name '*.py' -print -exec sed -i.bak 's/from client/from kinetic_sdk.generated.client/g' {} \;
	find src/kinetic_sdk/generated -name '*.bak' -print -exec rm {} \;
	rm -r src/kinetic_sdk/generated/{.openapi-generator,.gitignore,.gitlab-ci.yml,.openapi-generator-ignore,.travis.yml,README.md,git_push.sh,requirements.txt,setup.cfg,setup.py,test-requirements.txt,tox.ini}

build:
	poetry build
