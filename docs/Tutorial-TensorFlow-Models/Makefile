IMAGE_NAME = siaizu/tensorflow-models:v1.12.0-gpu
CONTAINER_NAME = siaizu_tensorflow_models

.PHONY: build
build:
	docker build . -t ${IMAGE_NAME}

.PHONY: run
run:
	docker run -i -t --gpus '"device=0"' \
		-v ${PWD}:/root/models/research/object_detection_tools \
		--name ${CONTAINER_NAME} \
		${IMAGE_NAME}
