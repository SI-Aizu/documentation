# Getting Started

```sh
cd ./docs/Tutorial-PyTorch
```



## Docker run

### CPU

Docker Compose

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



## Jupyter Lab

```sh
# コンテナ内
make jupyterlab
```
