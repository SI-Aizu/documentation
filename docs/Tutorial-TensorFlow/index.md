# Getting Started

```sh
# Build
docker build . -t siaizu/tensorflow:v2.2.0-gpu

# Run container
docker run -i -t --gpus all -v ${PWD}:/src --name siaizu_tensorflow siaizu/tensorflow:v2.2.0-gpu bash

# Remove container
docker container rm siaizu_tensorflow
```
