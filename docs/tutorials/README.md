# Tutorials チュートリアル

- [Transfer Learning - 転移学習](./transfer_learning/README.md)



## Getting started

### Docker Compose

```sh
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



## External Links

- [yoyoyo-yo/Gasyori100knock: 画像処理100本ノック](https://github.com/yoyoyo-yo/Gasyori100knock) - Image Processing 入門
- [yoyoyo-yo/DeepLearningMugenKnock: 深層学習無限ノック](https://github.com/yoyoyo-yo/DeepLearningMugenKnock) - Deep Learning 入門
- [言語処理100本ノック](http://www.cl.ecei.tohoku.ac.jp/nlp100/) - Natural Language Processing (NLP) 入門
- [arXivTimes/arXivTimes](https://github.com/arXivTimes/arXivTimes) - 論文の Abstract 要約を集めたリポジトリ

### Datasets

- [Food-101](https://www.vision.ee.ethz.ch/datasets_extra/food-101/)
- [zalandoresearch/fashion-mnist](https://github.com/zalandoresearch/fashion-mnist) - FMNIST 衣服データセット
- [DataSets - arXivTimes/arXivTimes](https://github.com/arXivTimes/arXivTimes/tree/master/datasets) - データセット一覧
- [ObjectNet](https://objectnet.dev/index.html) - ImageNet より難易度の高いテスト用データセット
- Logo ロゴ
    - [msn199959/Logo-2k-plus-Dataset: Logo-2k-plus-Dataset](https://github.com/msn199959/Logo-2k-plus-Dataset)
    - [LLD - Large Logo Dataset](https://data.vision.ee.ethz.ch/sagea/lld/)
    - [WebLogo-2M Dataset](http://www.eecs.qmul.ac.uk/~hs308/WebLogo-2M.html/)
    - [QMUL-OpenLogo](https://qmul-openlogo.github.io/)
    - [Flickr Logos dataset | IVA](http://image.ntua.gr/iva/datasets/flickr_logos/)
