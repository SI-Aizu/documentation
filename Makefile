pwd := $(CURDIR)
CONTAINER_NAME := pytorch
IMAGE_NAME := pytorch:latest
PORT := 8888
DOCKER_RUN := docker run -i -t -v $(pwd):/src --name $(CONTAINER_NAME) $(IMAGE_NAME)
DOCKER_RUN_PORT := docker run -i -t -v $(pwd):/src --name $(CONTAINER_NAME) -p $(PORT):$(PORT) $(IMAGE_NAME)

.PHONY: build
build:
	docker build . -t pytorch:latest

.PHONY: dev
dev:
	$(DOCKER_RUN) bash
