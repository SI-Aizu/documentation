# Getting Started

```sh
cd docs/Tutorial-TensorFlow
```



## Login to GitHub Packages

cf. [Docekr login - GitHub Packages](../Tutorial-GitHub/packages)



## Run Container

### CPU

docker-compose

```sh
# コンテナをバックグラウンドで起動
docker-compose up -d

# コンテナにログイン
docker-compose exec dev bash

# コンテナの終了と削除
docker-compose down
```

### GPU

```sh
make run
```



## JupyterLab

```sh
make lab
```
