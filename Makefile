# Build Configuration
# -------------------

APP_NAME := `sed -n 's/^ *name.*=.*"\([^"]*\)".*/\1/p' pyproject.toml`
APP_VERSION := `sed -n 's/^ *version.*=.*"\([^"]*\)".*/\1/p' pyproject.toml`


# Introspection Targets
# ---------------------

.PHONY: help
help: header targets

.PHONY: header
header:
	@echo "\033[34mEnvironment\033[0m"
	@echo "\033[34m---------------------------------------------------------------\033[0m"
	@printf "\033[33m%-23s\033[0m" "APP_NAME"
	@printf "\033[35m%s\033[0m" $(APP_NAME)
	@echo ""
	@printf "\033[33m%-23s\033[0m" "APP_VERSION"
	@printf "\033[35m%s\033[0m" $(APP_VERSION)
	@echo "\n"

.PHONY: targets
targets:
	@echo "\033[34mDevelopment Targets\033[0m"
	@echo "\033[34m---------------------------------------------------------------\033[0m"
	@perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-22s\033[0m %s\n", $$1, $$2}'


# Install Targets
# ----------------------------------------

.PHONY: install
install: ## Installs the Python dependencies
	poetry install
	poetry run pre-commit install
	poetry run pre-commit install --hook-type pre-commit --hook-type pre-push


# Script Execution Targets
# ----------------------------------------

.PHONY: cli-help
cli-help: ## Run the CLI tool with the help flag
	@poetry run python ./main.py --help

.PHONY: run
run: ## Run the CLI tool
	@poetry run python ./main.py


# Checking, Linting, and Formating Targets
# ----------------------------------------

.PHONY: lint-format
lint-format: lint-fix format ## Run linter and formatter

.PHONY: lint
lint: ## Run linter
	poetry run ruff check

.PHONY: lint-fix
lint-fix: ## Run linter and fix any minor issues
	poetry run ruff check --fix

.PHONY: format
format: ## Run code formatter
	poetry run ruff format

.PHONY: check-lockfile
check-lockfile: ## Compares lock file with pyproject.toml
	poetry check --lock


# Clean Targets
# ----------------------------------------

.PHONY: clean
clean: ## Deletes the .venv directory and the poetry.lock file
	rm -rf .venv && rm poetry.lock

.PHONY: clean-cache
clean-cache: ## Deletes all Python cache directories
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete && rm -rf .pytest_cache


# Publish Version Targets
# ----------------------------------------

.PHONY: version
version: ## Bump the version of the package and create a git tag
	@poetry version $(v)
	@git add pyproject.toml
	@git commit -m "v$$(poetry version -s)"
	@git tag v$$(poetry version -s)
	@git push
	@git push --tags
	@poetry version
