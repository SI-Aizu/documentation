# Tutorial

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

`config/ssd_inception_v2_coco.config` を編集することで前処理 (data augmentation) を追加・削除できる。

その他 batch size, learning rate などの設定もここで指定できる。



## Build Docker image

```sh
cd docs/Tutorial-TensorFlow-Models
```

```sh
# Build
make build
```



## Run Container

```sh
make run
```

コンテナにログインしたら以下を毎回実行する。

```sh
cd ~/models/research
export PYTHONPATH=${PYTHONPATH}:$(pwd):$(pwd)/slim
```

動作テスト

```sh
cd ~/models/research
python3 ./object_detection/builders/model_builder_test.py
```



## Train

ホストマシンで公開されている事前学習済みモデルをダウンロード。

```sh
cd models
bash get_ssd_inception_v2_coco_model.sh
```

コンテナ内。

```sh
nohup python3 ./object_detection/model_main.py \
    --pipeline_config_path="./object_detection_tools/config/ssd_inception_v2_coco.config" \
    --model_dir="./object_detection_tools/saved_model/cat_01" \
    --num_train_steps=20000 \
    --alsologtostderr > ./object_detection_tools/nohup.log &
```

`ctrl+p+q` でコンテナから抜ける。



## Tensorboard

```sh
cd docs/Tutorial-TensorFlow-Models/tensorboard
docker build . -t tensorboard:latest
docker run --rm -it -v ${PWD}/saved_model/cat_01:/logs -p 6006:6006 --network host --name tensorboard tensorboard:latest
```



## モデル変換

コンテナ内。

```sh
python3 ./object_detection/export_inference_graph.py \
    --input_type image_tensor \
    --pipeline_config_path ./object_detection_tools/config/ssd_inception_v2_coco.config \
    --output_directory ./object_detection_tools/exported_graphs/cat_01 \
    --trained_checkpoint_prefix ./object_detection_tools/saved_model/cat_01/model.ckpt-5555
cp ./object_detection_tools/scripts/convert_pbtxt_label.py .
python3 ./convert_pbtxt_label.py \
    -l='./object_detection_tools/data/tf_label_map.pbtxt' \
    > ./object_detection_tools/exported_graphs/cat_01/labels.txt
```



## 推論の実行

コンテナ内。

```sh
cd ~/models/research/object_detection_tools
python3 scripts/detect.py -i ./test.jpg
```
