# Tutorial



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
