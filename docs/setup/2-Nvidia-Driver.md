#Nvidia Driverの更新



- 古いドライバーと cuda を削除

```shell
$ sudo apt-get --purge remove nvidia-*
$ sudo apt-get --purge remove cuda-*
```

```
$ dpkg -l | grep nvidia
$ dpkg -l | grep cuda
```

で残りがないかを確認。



- ドライバーのリポジトリを追加。

   **control-C** を押さないこと。

```
sudo add-apt-repository ppa:graphics-drivers/ppa
```



- カーネルをアップデート。

- 推奨ドライバーを確認。

```
sudo apt-get update
ubuntu-drivers devices
```

を実行すると

```
driver    : nvidia-415 - thrid-party free
driver    : nvidia-430 - thrid-party free recommended
```

など(一部省略)が出力される。



- 先ほどの出力で推奨されたドライバーをインストールする

```
sudo apt-get install nvidia-430
```



- 再起動して、GPU が認識しているか確認

```
reboot
nvidia-smi
```

ここまでできたら勝ち

