IMAGE_NAME = docker.pkg.github.com/si-aizu/documentation/tensorflow-models
TAG = v2.3.0-gpu
CONTAINER_NAME = siaizu_tensorflow_models

.PHONY: run
run:
	# docker run -i -t --gpus all
	docker run -i -t --gpus '"device=0"' \
		-v ${PWD}:/home//tensorflow/models/research/object_detection/siaizu \
		--name ${CONTAINER_NAME} \
		${IMAGE_NAME}:${TAG}

.PHONY: run-gpu1
run-gpu1:
	docker run -i -t --gpus '"device=1"' \
		-v ${PWD}:/home//tensorflow/models/research/object_detection/siaizu \
		--name ${CONTAINER_NAME}_gpu1 \
		${IMAGE_NAME}:${TAG}
