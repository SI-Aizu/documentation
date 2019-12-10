## Deep Learning Tutorial with PyTorch

- [PyTorch](https://pytorch.org/)



## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Deep Learning Tutorial with PyTorch](#deep-learning-tutorial-with-pytorch)
- [Setup](#setup)
  - [Install Docker](#install-docker)
    - [macOS](#macos)
    - [Ubuntu 18.04](#ubuntu-1804)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

*TOC is generated with [DocToc](https://github.com/thlorenz/doctoc).*



## Getting started

```sh
git clone git@github.com:SI-Aizu/deep-learning-tutorial.git
cd ./deep-learning-tutorial

# コンテナをビルドしてバックグラウンドで起動
docker-compose up -d --build

# コンテナにログイン
docker-compose exec dev bash

# コンテナの終了と削除
docker-compose down
```



## Setup

### Install Docker

`which docker` や `which docker-compose` などで確認し、インストールされていなければ以下のようにインストールする。
macOS の場合 **Docker for Mac** は `docker-compose` も含んでいる。

#### macOS

> [Install Docker Desktop on Mac | Docker Documentation](https://docs.docker.com/docker-for-mac/install/)

#### Ubuntu 18.04

Rootless Docker をオススメする。

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
docker run hello-world
```

続いて Docker Compose のインストール。

> [Install Docker Compose | Docker Documentation](https://docs.docker.com/compose/install/)

```console
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose

$ docker-compose --version
docker-compose version 1.25.0, build 0a186604
```
