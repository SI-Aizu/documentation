# Docker


## Installation

`which docker` や `which docker-compose` などで確認し、インストールされていなければ以下のようにインストールする。
macOS の場合 **Docker for Mac** は `docker-compose` も含んでいる。

### macOS

> [Install Docker Desktop on Mac | Docker Documentation](https://docs.docker.com/docker-for-mac/install/)

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

### Ubuntu 18.04 Rootless

Rootless Docker はオススメ。

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
