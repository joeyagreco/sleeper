PYTEST_ARGS=

.PHONY: deps
deps:
	@python -m pip install -r requirements.dev.txt
	@python -m pip install -r requirements.txt

.PHONY: fmt
fmt:
	@ruff check --fix
	@ruff format

.PHONY: fmt-check
fmt-check:
	@ruff check
	@ruff format --check

.PHONY: test-all
test-all:
	@make test-unit $(PYTEST_ARGS)
	@make test-integration $(PYTEST_ARGS)

.PHONY: test-unit
test-unit:
	@pytest test/unit $(PYTEST_ARGS)

.PHONY: test-integration
test-integration:
	@pytest test/integration $(PYTEST_ARGS)

.PHONY: pkg-build
pkg-build:
	@rm -rf build
	@rm -rf dist
	@python setup.py sdist bdist_wheel

.PHONY: pkg-test
pkg-test: pkg-build
	@python -m twine upload --repository testpypi dist/*

.PHONY: pkg-prod
pkg-prod: pkg-build
	@python -m twine upload dist/*
