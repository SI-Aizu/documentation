# Tutorial

TensorFlow v2.3.0

Inception v2 base SSD 300 の転移学習 (Transfer Learning)

- [tensorflow/models: Models and examples built with TensorFlow](https://github.com/tensorflow/models)
- [Tensorflow Object Detection API v1.13.0](https://github.com/tensorflow/models/tree/v1.13.0/research/object_detection)
- [Installation - Tensorflow Object Detection API v1.13.0](https://github.com/tensorflow/models/blob/v1.13.0/research/object_detection/g3doc/installation.md)
- [model zoo - Tensorflow Object Detection API v1.13.0](https://github.com/tensorflow/models/blob/v1.13.0/research/object_detection/g3doc/detection_model_zoo.md)



## Prepare dataset

### train val

`.tfrecord` を以下のように配置。

- `data/train`: 教師データ
- `data/val`: 検証データ

```console
$ tree data
data
├── change_tfrecord_filename.sh
├── cat-TFRecords-export
├── tf_label_map.pbtxt
├── train
│   ├── frame-fa9aee7507d749368eaea01fde15dc0f.tfrecord
│   ├── frame-fb52802ac5fb1d0e4465c535603cc8d1.tfrecord
│   ├── frame-fcca1acaa65736d0632a4c9d09f46f34.tfrecord
...
│   └── frame-fe032dbfda72e3a42d0a9b00b62695fe.tfrecord
└── val
    ├── frame-fe8158671dbeda266efea62af20d7e97.tfrecord
    ├── frame-ffef9a9882b57f2c6124c889a3ec9afd.tfrecord
    ├── frame-ffef9a9882b57f2c6124c889a3ec9afd.tfrecord
...
```

`cat-TFRecords-export` にすべての tfrecord が入っているものとして、

```sh
cd docs/Tutorial-TensorFlow-Models/data
bash ./change_tfrecord_filename.sh cat-TFRecords-export
```

あとは `train` と `val` に tfrecord を分けて配置する。

### tf_label_map.pbtxt

```
item {
 id: 1
 name: 'cat'
}
```



## config

`config/ssd_resnet50_v1_fpn_640x640_coco17_tpu-8.config` を編集することで前処理 (data augmentation) を追加・削除できる。

その他 batch size, learning rate などの設定もここで指定できる。

- `num_classes`: number of classes
- `fine_tune_checkpoint`: pre-trained model
- `num_steps` Maximum number of steps
- `data_augmentation_options` 画像の前処理・水増し



## Pull Docker image

### Login to GitHub Packages

cf. [Docekr login - GitHub Packages](../Tutorial-GitHub/packages)

### Pull

```sh
cd docs/Tutorial-TensorFlow-Models
```

```sh
# Build
docker-compose pull
```



## Run Container

### CPU

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

### 動作確認

```sh
cd /src/models/research
python object_detection/builders/model_builder_tf2_test.py
```



## Train

ホストマシンで公開されている事前学習済みモデルをダウンロード。

```sh
cd models
bash ssd_resnet50_v1_fpn_640x640_coco17_tpu-8.sh
```

コンテナ内。

```sh
cd /src/models/research
nohup python3 ./object_detection/model_main_tf2.py \
    --pipeline_config_path="./object_detection/siaizu/config/ssd_resnet50_v1_fpn_640x640_coco17_tpu-8.config" \
    --model_dir="./object_detection/siaizu/saved_model/cat_01" \
    --alsologtostderr > ./object_detection/siaizu/nohup.log &
```

`ctrl+p+q` でコンテナから抜ける。



## Tensorboard

```sh
docker run --rm -i -t \
  -v ${PWD}/saved_model/cat_01:/logs \
  -p 6006:6006 \
  --net host \
  --name siaizu_tensorflow_models_tensorboard \
  docker.pkg.github.com/si-aizu/documentation/tensorflow-models:v2.3.0-gpu \
  tensorboard --logdir /logs
```



## モデル変換

コンテナ内。

```sh
python3 ./object_detection/export_inference_graph.py \
    --input_type image_tensor \
    --pipeline_config_path ./object_detection/siaizu/config/ssd_resnet50_v1_fpn_640x640_coco17_tpu-8.config \
    --output_directory ./object_detection/siaizu/exported_graphs/cat_01 \
    --trained_checkpoint_prefix ./object_detection/siaizu/saved_model/cat_01/model.ckpt-5555
cp ./object_detection/siaizu/scripts/convert_pbtxt_label.py .
python3 ./convert_pbtxt_label.py \
    -l='./object_detection/siaizu/data/tf_label_map.pbtxt' \
    > ./object_detection/siaizu/exported_graphs/cat_01/labels.txt
```



## 推論の実行

コンテナ内。

```sh
cd ~/models/research/siaizu
python3 scripts/detect.py -i ./test.jpg
```
