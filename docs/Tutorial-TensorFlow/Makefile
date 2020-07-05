IMAGE_NAME = docker.pkg.github.com/si-aizu/documentation/tensorflow
TAG = v2.2.0-gpu
CONTAINER_NAME = siaizu_tensorflow

.PHONY: build
build:
	docker build . \
		--cache-from=${IMAGE_NAME}:${TAG} \
		-t ${IMAGE_NAME}:${TAG}

.PHONY: run
run:
	docker run -i -t --gpus all \
		-v ${PWD}:/src \
		--name ${CONTAINER_NAME} \
		${IMAGE_NAME}:${TAG} \
		bash

.PHONY: pull
pull:
	docker pull ${IMAGE_NAME}:${TAG}

.PHONY: push
push:
	docker push ${IMAGE_NAME}:${TAG}
