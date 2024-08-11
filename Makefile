include .env.example

.PHONY: format
format:
	ruff check --select I --fix .
	ruff check --fix .
	ruff format .

.PHONY: check_lint
check_lint:
	ruff format --check .
	ruff check .

.PHONY: install_requirements_dev
install_requirements_dev:
	uv pip install -r requirements_dev.txt

.PHONY: check_migrations
check_migrations:
	python manage.py makemigrations --check --dry-run --verbosity 3

.PHONY: tests
tests:
	set -a && source .env.example && set +a; \
	pytest -x --cov --junitxml=junit.xml


.PHONY: up_services
up_services:
	cp .env.example .env; \
	docker compose up -d

.PHONY: clean
clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.mo' `
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf *.egg-info
	rm -rf apps/*.egg-info
	rm -f .coverage
	rm -f .coverage.*
	rm -rf build
	rm -rf dist
	rm -rf deploy_dist
