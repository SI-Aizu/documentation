# 3. Docker



## Install Docker

`which docker` や `which docker-compose` などで確認し、インストールされていなければインストールする。

### macOS

> [Install Docker Desktop on Mac | Docker Documentation](https://docs.docker.com/docker-for-mac/install/)

!!! note "To macOS users"
    macOS の場合 **Docker for Mac** は `docker-compose` も含んでいる。

### Ubuntu 18.04

公式ドキュメントに従って Docker をインストール。

> [Install Docker Engine on Ubuntu | Docker Documentation](https://docs.docker.com/engine/install/ubuntu/)

続いて Docker Compose のインストール。

> [Install Docker Compose | Docker Documentation](https://docs.docker.com/compose/install/)

compose のインストールに利用するツールをインストールする。

```sh
sudo apt install -y curl jq
```

以下のコマンドで compose (v2) のインストールとアップグレードができる。

```sh
export COMPOSE_VERSION=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
curl -L "https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o "${HOME}/.docker/cli-plugins/docker-compose" && \
    chmod a+x "${HOME}/.docker/cli-plugins/docker-compose" && \
    docker compose version
```



## Install nvidia-docker

### nvidia-docker

- [NVIDIA/nvidia-docker: Build and run Docker containers leveraging NVIDIA GPUs](https://github.com/NVIDIA/nvidia-docker)

一応実行するコマンドを下に書いておくが、上記を見て最新の情報を確認すること。

```sh
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

sudo apt update && sudo apt install -y nvidia-container-toolkit
sudo systemctl restart docker
```



## Container から GPU を利用する

`nvidia-smi` で確認できる CUDA version と docker image tag の CUDA version を一致させる必要がある。

```sh
docker run --rm -i -t --gpus all nvidia/cuda:10.2-base-ubuntu18.04 bash
```

コンテナ内で `nvidia-smi` を実行して GPU status を確認できれば問題ない。

### PyTorch で GPU を確認

`python3` を実行してインタラクティブモードで確認する。

```py
>>> import torch
>>> print(torch.cuda.is_available())
True
>>> torch.cuda.get_device_name(0)
'GeForce RTX 2080'
```

### TensorFlow で GPU を確認

`python3` を実行してインタラクティブモードで確認する。

```py
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
```

上記を実行すると以下のように利用できるデバイスの一覧を確認できる。

```
2020-06-06 04:53:00.588924: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1247] Created TensorFlow device (/device:GPU:0 with 10091 MB memory) -> physical GPU (device: 0, name: GeForce RTX 2080 Ti, pci bus id: 0000:17:00.0, compute capability: 7.5)
2020-06-06 04:53:00.590217: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1247] Created TensorFlow device (/device:GPU:1 with 10202 MB memory) -> physical GPU (device: 1, name: GeForce RTX 2080 Ti, pci bus id: 0000:65:00.0, compute capability: 7.5)
```
