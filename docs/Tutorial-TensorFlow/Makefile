IMAGE_NAME = docker.pkg.github.com/si-aizu/documentation/tensorflow
TAG = v2.2.0-gpu
CONTAINER_NAME = siaizu_tensorflow

.PHONY: run
run:
	docker run -i -t --gpus '"device=0"' \
		-v ${PWD}:/src \
		-p 8000:8000 \
		--name ${CONTAINER_NAME} \
		${IMAGE_NAME}:${TAG} \
		bash

.PHONY: lab
lab:
	jupyter-lab --port 8000 --ip=0.0.0.0 --allow-root
