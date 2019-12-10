pwd := $(CURDIR)
CONTAINER_NAME := pytorch
IMAGE_NAME := pytorch:latest
PORT := 8888
DOCKER_RUN := docker run -i -t -v $(pwd):/src --name $(CONTAINER_NAME) $(IMAGE_NAME)
DOCKER_RUN_PORT := docker run -i -t -v $(pwd):/src --name $(CONTAINER_NAME) -p $(PORT):$(PORT) $(IMAGE_NAME)

.PHONY: buildcpu
buildcpu:
	docker build . -t pytorch:latest

.PHONY: dev
dev:
	$(DOCKER_RUN) bash

.PHONY: devrm
devrm:
	docker container stop $(CONTAINER_NAME)
	docker container rm $(CONTAINER_NAME)

