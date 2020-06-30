# 2. NVIDIA Driver

!!! note "To Docker user"
    Docker container から GPU を利用する場合は CUDA や cuDNN をホストマシンにインストールする必要はないので、
    CUDA の部分は関係ない。

!!! warning "注意"
    `ctrl-c` などで作業を中断しないように気をつけること。



## Installation

### NVIDIA Driver

```sh
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update
ubuntu-drivers devices
```

```console
$ ubuntu-drivers devices
== /sys/devices/pci0000:16/0000:16:00.0/0000:17:00.0 ==
modalias : pci:v000010DEd00001E07sv00001043sd00008666bc03sc00i00
vendor   : NVIDIA Corporation
driver   : nvidia-driver-435 - distro non-free
driver   : nvidia-driver-440 - third-party free recommended
driver   : nvidia-driver-415 - third-party free
driver   : nvidia-driver-410 - third-party free
driver   : xserver-xorg-video-nouveau - distro free builtin
```

recommended のものをインストールする。

```sh
sudo apt install -y nvidia-driver-440
sudo reboot
```

再起動後に `nvidia-smi` で GPU status を取得できれば成功。

```console
$ nvidia-smi
Sat Jun  6 13:22:56 2020
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 440.82       Driver Version: 440.82       CUDA Version: 10.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce RTX 208...  Off  | 00000000:17:00.0 Off |                  N/A |
| 24%   35C    P8    14W / 250W |    119MiB / 11018MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+

...
```

### CUDA cuDNN

conda もしくは nvidia-docker を利用する場合は CUDA や cuDNN のインストールは不要。



## Upgrade

### 古いドライバーと cuda を削除

```sh
sudo apt --purge remove 'nvidia-*'
sudo apt --purge remove 'cuda-*'
```

```sh
dpkg -l | grep nvidia
dpkg -l | grep cuda
```

で残りがないかを確認。   

もし cuda で残りがあったら `autoremove` で削除を試みる。 

```sh
sudo apt autoremove cuda
```

これでもまだ消えない場合には個別に `remove` する。

### 新しいドライバーのインストール


リポジトリを追加して、パッケージ一覧をアップデートした後に、推奨ドライバーを確認する。

```sh
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update
ubuntu-drivers devices
```

を実行すると

```
driver    : nvidia-415 - thrid-party free
driver    : nvidia-430 - thrid-party free recommended
```

など(一部省略)が出力されるので、推奨 (recommended) されたドライバーをインストールする。

```sh
sudo apt install -y nvidia-430
```

再起動した後に GPU が認識できるか確認する。

```sh
sudo reboot
nvidia-smi
```

ここまでできたら勝ち。
