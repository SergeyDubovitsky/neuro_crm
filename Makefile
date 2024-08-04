manage = python manage.py


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
	$(manage) makemigrations --check --dry-run --verbosity 3

.PHONY: tests
tests:
	pytest --cov
