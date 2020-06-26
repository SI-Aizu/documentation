IMAGE_NAME = siaizu/tensorflow-models:v2.2.0-gpu
CONTAINER_NAME = siaizu_tensorflow_models

.PHONY: build
build:
	docker build . -t ${IMAGE_NAME}

.PHONY: run
run:
	docker run -i -t --gpus all \
		-v ${PWD}:/src \
		--name ${CONTAINER_NAME} \
		${IMAGE_NAME} \
		bash
