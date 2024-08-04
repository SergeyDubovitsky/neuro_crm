include .env.example

.PHONY: lint
lint:
	ruff check --select I --fix .
	ruff check --fix .
	ruff format .

.PHONY: check_lint
check_lint:
	ruff format --check .
	ruff check .

.PHONY: check_migrations
check_migrations:
	python manage.py makemigrations --check --dry-run --verbosity 3

.PHONY: tests
tests:
	cp -n .env.example .env; \
	set -a && source .env && set +a; \
	pytest -x --cov
