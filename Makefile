.PHONY: lint
lint:
	ruff check --select I --fix .
	ruff check --fix .
	ruff format .

check_lint:
	ruff format --check .
	ruff check .
