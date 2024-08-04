.PHONY: lint
lint:
	ruff check --select I --fix .
	ruff check --fix .
	ruff format .
