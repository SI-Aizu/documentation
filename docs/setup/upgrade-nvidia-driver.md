# NVIDIA Driver の更新

!!! note "To Docker user"
    Docker container から GPU を利用する場合は CUDA や cuDNN をホストマシンにインストールする必要はないので、
    CUDA の部分は関係ない。


## 古いドライバーと cuda を削除

```sh
sudo apt-get --purge remove nvidia-*
sudo apt-get --purge remove cuda-*
```

```sh
dpkg -l | grep nvidia
dpkg -l | grep cuda
```

で残りがないかを確認。


## 新しいドライバーのインストール

このとき `ctrl-c` などで作業を中断しないように気をつけること。

```sh
sudo add-apt-repository ppa:graphics-drivers/ppa
```

パッケージ一覧をアップデートした後に、推奨ドライバーを確認する。

```sh
sudo apt-get update
ubuntu-drivers devices
```

を実行すると

```
driver    : nvidia-415 - thrid-party free
driver    : nvidia-430 - thrid-party free recommended
```

など(一部省略)が出力されるので、推奨 (recommended) されたドライバーをインストールする。

```sh
sudo apt-get install -y nvidia-430
```

再起動した後に GPU が認識できるか確認する。

```sh
sudo reboot
nvidia-smi
```

ここまでできたら勝ち。