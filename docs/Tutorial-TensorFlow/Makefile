IMAGE_NAME = siaizu/tensorflow:v2.2.0-gpu
CONTAINER_NAME = siaizu_tensorflow

.PHONY: build
build:
	docker build . -t ${IMAGE_NAME}

.PHONY: run
run:
	docker run -i -t --gpus '"device=0"' \
		-v ${PWD}:/src \
		--name ${CONTAINER_NAME} \
		${IMAGE_NAME} \
		bash
