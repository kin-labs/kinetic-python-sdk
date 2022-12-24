clean:
	rm -rf dist build __pycache__ *.egg-info

build:
	poetry build

format:
	poetry run isort src tests
	poetry run black --line-length=120 src tests

lint:
	poetry run black --check --diff --line-length=120 src tests
	#poetry run pydocstyle src tests
	poetry run flake8 src tests
	#poetry run mypy src
	poetry run pylint --rcfile=.pylintrc src tests

generate:
	rm -r src/kinetic_sdk/generated && openapi-generator-cli generate -i https://raw.githubusercontent.com/kin-labs/kinetic/dev/api-swagger.json -g python -o src/kinetic_sdk/generated --additional-properties=packageName=client --global-property=modelTests=false,apiTests=false,modelDocs=false,apiDocs=false
	find src/kinetic_sdk/generated -name '*.py' -print -exec sed -i.bak 's/from client/from kinetic_sdk.generated.client/g' {} \;
	find src/kinetic_sdk/generated -name '*.bak' -print -exec rm {} \;
	rm -r src/kinetic_sdk/generated/{.openapi-generator,.gitignore,.gitlab-ci.yml,.openapi-generator-ignore,.travis.yml,README.md,git_push.sh,requirements.txt,setup.cfg,setup.py,test-requirements.txt,tox.ini}

install:
	poetry install

test:
	poetry run pytest -vv -s ./tests/
