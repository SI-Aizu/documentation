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

以下のコマンドで compose のインストールとアップグレードができる。

```sh
export DOCKER_COMPOSE_VERSION=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
sudo curl -L "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
    sudo chmod +x /usr/local/bin/docker-compose && \
    docker-compose --version
```



## Install Rootless Docker

Ubuntu のみ。

Rootless Docker もオススメ。

> [Docker 19.03新機能 (root権限不要化、GPU対応強化、CLIプラグイン) - nttlabs - Medium](https://medium.com/nttlabs/docker-1903-5155754ff8ac)

```sh
cd ~
sudo apt update
sudo apt upgrade -y
sudo apt install -y curl uidmap
curl -fsSL https://get.docker.com/rootless | sh
```

以下を `~/.bashrc` に追記する。

```sh
# Rootless Docker
export PATH="${HOME}/bin:${PATH}"
export DOCKER_HOST="unix:///run/user/1000/docker.sock"
```

```sh
# ~/.bashrc への変更を反映するために Bash を再起動
exec bash

# Docker daemon を起動
systemctl --user start docker

# Docker の動作確認
docker run --rm -it hello-world
```

マシンを再起動した後は再び `systemctl --user start docker` を実行する必要がある。
でないと次のようなエラーメッセージが表示されて docker を実行できない。

```
Cannot connect to the Docker daemon at unix:///run/user/1000/docker.sock. Is the docker daemon running?
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

### Notes for Rootless Docker

- [nvidia-container-runtime doesn't work with rootless mode · Issue #38729 · moby/moby](https://github.com/moby/moby/issues/38729)

現在 Rootless Docker から GPU を利用するには上記リンク先のような対応が必要。

```sh
sudo vim /etc/nvidia-container-runtime/config.toml
```

具体的には上記ファイルを以下のように書き換える。

```diff
- #no-cgroups = false
+ no-cgroups = true
```



## Container から GPU を利用する

`nvidia-smi` で確認できる CUDA version と docker image tag の CUDA version を一致させる必要がある。

```sh
docker run --rm -i -t --gpus all nvidia/cuda:10.2-devel-ubuntu18.04 bash
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
