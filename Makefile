manage = python manage.py


.PHONY: lint
lint:
	ruff check --select I --fix .
	ruff check --fix .
	ruff format .

check_lint:
	ruff format --check .
	ruff check .

check_migrations:
	$(manage) makemigrations --check --dry-run --verbosity 3
