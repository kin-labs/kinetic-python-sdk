install:
	poetry install

test:
	poetry run pytest -s

start:
	poetry run python src

generate:
	rm -r src/generated && openapi-generator-cli generate -i https://raw.githubusercontent.com/kin-labs/kinetic/dev/api-swagger.json -g python -o src/generated

clean:
	rm -rf /Users/alexramirez/Library/Caches/pypoetry/virtualenvs/*

dev_sdk:
	cd kinetic-sdk/kinetic_sdk && nodemon --exec python3 __main__.py
