COMPOSE = docker-compose
COMPOSE_BASE_COMMAND = ${COMPOSE} run --rm dev

.PHONY: build
build:
	${COMPOSE} build

.PHONY: run
run:
	${COMPOSE_BASE_COMMAND} bash

.PHONY: fmt
fmt:
	${COMPOSE_BASE_COMMAND} black .

.PHONY: cifmt
cifmt:
	${COMPOSE_BASE_COMMAND} black --check --diff .

.PHONY: lint
lint:
	${COMPOSE_BASE_COMMAND} flake8 --show-source
