install_demo:
	cd demo && poetry install

install_sdk:
	cd kinetic-sdk && poetry install

install_open:
	cd kinetic-sdk/kinetic_sdk/generated/openapi-client && poetry install

run_demo:
	cd demo && poetry run python demo

run_sdk:
	cd kinetic-sdk && poetry run python kinetic_sdk

generate:
	openapi-generator-cli generate -i ./api-swagger.json -g python -o kinetic-sdk/kinetic_sdk/generated

clean:
	rm -rf /Users/alexramirez/Library/Caches/pypoetry/virtualenvs/*

all:
	make install_open
	make install_sdk
	make install_demo

restart_demo:
	make clean
	make all
	make run_demo

restart_sdk:
	make clean
	make install_open
	make install_sdk
	make run_sdk

dev_sdk:
	cd kinetic-sdk/kinetic_sdk && nodemon --exec python3 __main__.py