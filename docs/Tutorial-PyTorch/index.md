# Getting Started


## Docker Compose

```sh
cd ./docs/Tutorial-PyTorch

# コンテナをビルド
docker-compose build

# コンテナをバックグラウンドで起動
docker-compose up -d

# コンテナにログイン
docker-compose exec dev bash

# コンテナの終了と削除
docker-compose down
```

## Jupyter Lab

```sh
# コンテナ内
cd ./transfer_learning
jupyter-lab --ip=0.0.0.0 --no-browser --allow-root
```
