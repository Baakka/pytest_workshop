.PHONY: help init install lint fmt fmt-check test test-ci clean

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

init: ## Initialize the development environment
	uv sync --dev

install: ## Install the project in development mode
	uv pip install -e ".[dev]"

lint: ## Run ruff linter
	uv run ruff check .

fmt: ## Format code with ruff
	uv run ruff format .

fmt-check: ## Check code formatting with ruff
	uv run ruff format --check .

test: ## Run tests
	uv run pytest

test-ci: ## Run tests with coverage for CI
	uv run pytest --cov=src --cov-report=xml --cov-report=html --cov-report=term --junit-xml=reports/pytest.xml --cov-report=html:reports/coverage

clean: ## Clean up generated files
	rm -rf .pytest_cache/
	rm -rf reports/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -f coverage.xml
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete