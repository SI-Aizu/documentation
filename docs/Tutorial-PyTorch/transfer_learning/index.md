# 転移学習

> [Transfer Learning for Computer Vision Tutorial — PyTorch Tutorials 1.11.0+cu102 documentation](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)

学習済み ResNet18 を用いて転移学習をするチュートリアル。

1. 全層を再学習する (Fine tuning と呼ばれる)
2. 全結合層のみを再学習する (こっちを指して転移学習と呼ぶこともある)

```sh
wget https://pytorch.org/tutorials/_downloads/62840b1eece760d5e42593187847261f/transfer_learning_tutorial.ipynb
```

```sh
wget "https://download.pytorch.org/tutorial/hymenoptera_data.zip"
unzip hymenoptera_data.zip
rm hymenoptera_data.zip
mkdir data
mv hymenoptera_data data/
```
