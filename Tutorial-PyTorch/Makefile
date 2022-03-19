.PHONY: run
run:
	sudo docker run --rm -i -t --gpus all -v ${PWD}:/src -p 8000:8000 docker.pkg.github.com/si-aizu/documentation/pytorch:v1.11.0

.PHONY: lab
lab:
	jupyter-lab --port 8000 --ip=0.0.0.0 --allow-root
