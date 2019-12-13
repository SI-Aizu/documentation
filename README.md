## Deep Learning Tutorial with PyTorch

研究室の新規メンバー向けの教材。以下を学ぶ。

- Deep Learning 深層学習
- Python
- Git, GitHub
- Docker
- Ubuntu, GPU

Deep Learning framework は主に [PyTorch] を取り扱う。

[PyTorch]: https://pytorch.org/



## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Links](#links)
  - [Internal](#internal)
  - [External](#external)
  - [Datasets](#datasets)
- [Getting started](#getting-started)
  - [Git and Docker](#git-and-docker)
  - [Jupyter Lab](#jupyter-lab)
- [Setup Docker](#setup-docker)
  - [macOS](#macos)
  - [Ubuntu 18.04](#ubuntu-1804)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

*TOC is generated with [DocToc](https://github.com/thlorenz/doctoc).*



## Links

### Internal

- [チュートリアル一覧](./tutorials/README.md) - このリポジトリのチュートリアル一覧

### External

- [yoyoyo-yo/Gasyori100knock: 画像処理100本ノック](https://github.com/yoyoyo-yo/Gasyori100knock) - Image Processing 入門
- [yoyoyo-yo/DeepLearningMugenKnock: 深層学習無限ノック](https://github.com/yoyoyo-yo/DeepLearningMugenKnock) - Deep Learning 入門
- [言語処理100本ノック](http://www.cl.ecei.tohoku.ac.jp/nlp100/) - Natural Language Processing (NLP) 入門
- [arXivTimes/arXivTimes](https://github.com/arXivTimes/arXivTimes) - 論文の Abstract 要約を集めたリポジトリ

### Datasets

- [zalandoresearch/fashion-mnist](https://github.com/zalandoresearch/fashion-mnist) - FMNIST 衣服データセット
- [DataSets - arXivTimes/arXivTimes](https://github.com/arXivTimes/arXivTimes/tree/master/datasets) - データセット一覧
- [ObjectNet](https://objectnet.dev/index.html) - ImageNet より難易度の高いテスト用データセット



## Getting started

### Git and Docker

```sh
git clone git@github.com:SI-Aizu/deep-learning-tutorial.git
cd ./deep-learning-tutorial

# コンテナをビルド
docker-compose build

# コンテナをバックグラウンドで起動
docker-compose up -d

# コンテナにログイン
docker-compose exec dev bash

# コンテナの終了と削除
docker-compose down
```

### Jupyter Lab

```sh
# コンテナ内
cd ./tutorials/transfer_learning
jupyter-lab --ip=0.0.0.0 --no-browser --allow-root
```



## Setup Docker

`which docker` や `which docker-compose` などで確認し、インストールされていなければ以下のようにインストールする。
macOS の場合 **Docker for Mac** は `docker-compose` も含んでいる。

### macOS

> [Install Docker Desktop on Mac | Docker Documentation](https://docs.docker.com/docker-for-mac/install/)

### Ubuntu 18.04

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
