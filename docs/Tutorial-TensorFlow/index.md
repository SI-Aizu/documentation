# Getting Started



## Build Docker image

```sh
# Build
docker build . -t siaizu/tensorflow:v2.2.0-gpu
```

ビルド済み docker image を公開しているので build せずに run でも良い。

- [siaizu/tensorflow - Docker Hub](https://hub.docker.com/r/siaizu/tensorflow)



## Run Container

```sh
docker run -i -t --gpus all -v ${PWD}:/src --name siaizu_tensorflow siaizu/tensorflow:v2.2.0-gpu bash
```
