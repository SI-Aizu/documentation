IMAGE_NAME = docker.pkg.github.com/si-aizu/documentation/tensorflow-models
TAG = v2.3.0-gpu
CONTAINER_NAME = siaizu_tensorflow_models

.PHONY: run
run:
	docker run -i -t --gpus '"device=0"' \
		-v ${PWD}:/src/models/research/object_detection/siaizu \
		--name ${CONTAINER_NAME} \
		${IMAGE_NAME}:${TAG}
