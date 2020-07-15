DOCKER_IMAGE_NAME := docker.pkg.github.com/si-aizu/documentation/pytorch
DOCKER_TAG := v1.5.1
DOCKER_CONTAINER_NAME := siaizu_documentation_pytorch

.PHONY: run
run:
	docker run -i -t --gpus '"device=0"' \
		-v ${PWD}:/src \
		-p 8000:8000 \
		--name ${DOCKER_CONTAINER_NAME} \
		${DOCKER_IMAGE_NAME}:${DOCKER_TAG} \
		bash

.PHONY: jupyterlab
jupyterlab:
	jupyter-lab --port 8000 --ip=0.0.0.0 --allow-root
