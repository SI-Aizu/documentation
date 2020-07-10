# 1. Ubuntu


## Create Boot USB Disk

- [balenaEtcher - Flash OS images to SD cards & USB drives](https://www.balena.io/etcher/)

balenaEtcher が便利。


## Install Ubuntu

[Install Ubuntu desktop | Ubuntu](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)


## Upgrade dependencies

定期的に以下を実行して、ツール等を最新版に更新した方がよい。

```sh
# ソフトウェア一覧の更新
sudo apt update

# 更新可能な依存の一覧を表示
apt list --upgradable

# 更新可能な依存を更新
sudo apt upgrade -y
```
