# Darknet YOLO v3 and v4

- v4 Paper: [[2004.10934] YOLOv4: Optimal Speed and Accuracy of Object Detection](https://arxiv.org/abs/2004.10934)
- Repository: [AlexeyAB/darknet: YOLOv4 - Neural Networks for Object Detection (Windows and Linux version of Darknet )](https://github.com/AlexeyAB/darknet)
- Google Colab: [YOLOv4_Tutorial.ipynb - Colaboratory](https://colab.research.google.com/drive/12QusaaRj_lUwCGDvQNfICpa7kA7_a2dE)



## Build Docker Image

### Edit Makefile

利用する GPU ごとに `Makefile` を編集する必要がある。

GeForce RTX 2080 Ti であれば以下のようにする。(デフォルト)

```Makefile
# GeForce RTX 2080 Ti, RTX 2080, RTX 2070, Quadro RTX 8000, Quadro RTX 6000, Quadro RTX 5000, Tesla T4, XNOR Tensor Cores
ARCH= -gencode arch=compute_75,code=[sm_75,compute_75]

# GTX 1080, GTX 1070, GTX 1060, GTX 1050, GTX 1030, Titan Xp, Tesla P40, Tesla P4
# ARCH= -gencode arch=compute_61,code=sm_61 -gencode arch=compute_61,code=compute_61
```

GTX 1080 であれば以下のようにする。

```Makefile
# GeForce RTX 2080 Ti, RTX 2080, RTX 2070, Quadro RTX 8000, Quadro RTX 6000, Quadro RTX 5000, Tesla T4, XNOR Tensor Cores
# ARCH= -gencode arch=compute_75,code=[sm_75,compute_75]

# GTX 1080, GTX 1070, GTX 1060, GTX 1050, GTX 1030, Titan Xp, Tesla P40, Tesla P4
ARCH= -gencode arch=compute_61,code=sm_61 -gencode arch=compute_61,code=compute_61
```

### Build

```console
$ nvidia-smi
NVIDIA-SMI 440.82       Driver Version: 440.82       CUDA Version: 10.2
```

`nvidia-smi` で確認できる CUDA Version と Base Docker image `nvidia/cuda` の tag を一致させる。

```sh
sudo docker build . -t darknet-yolo:latest --build-arg BASE_IMAGE="nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04"
```



## Run Container

```sh
sudo docker run --rm -i -t --gpus all darknet-yolo:latest bash
```



## Predict

推論の実行例を以下に示す。

```console
$ ./darknet detector test cfg/coco.data cfg/yolov3.cfg yolov3.weights data/dog.jpg
...
data/dog.jpg: Predicted in 12.776000 milli-seconds.
bicycle: 99%
dog: 100%
truck: 94%
...
```

```console
$ ./darknet detector test cfg/coco.data cfg/yolov4.cfg yolov4.weights data/dog.jpg
...
data/dog.jpg: Predicted in 24.482000 milli-seconds.
bicycle: 92%
dog: 98%
truck: 92%
pottedplant: 33%
...
```

```console
$ python3 darknet.py
...
Total BFLOPS 128.459
avg_outputs = 1068395
 Allocate additional workspace_size = 52.43 MB
 Try to load weights: yolov4.weights
Loading weights from yolov4.weights...
 seen 64, trained: 32032 K-images (500 Kilo-batches_64)
Done! Loaded 162 layers from weights-file
Loaded - names_list: data/coco.names, classes = 80
Unable to show image: No module named 'skimage'
[('dog', 0.9787506461143494, (220.98822021484375, 383.2079772949219, 184.41787719726562, 316.5090637207031)), ('bicycle', 0.921798586845398, (343.4819641113281, 276.87603759765625, 458.0648193359375, 298.7120361328125)), ('truck', 0.91830974817276, (574.2606201171875, 123.24830627441406, 220.67361450195312, 93.20550537109375)), ('pottedplant', 0.33072134852409363, (699.3265380859375, 131.88845825195312, 36.533931732177734, 45.44673538208008))]
```

| v3 | v4 |
|---|---|
| ![yolov3](https://user-images.githubusercontent.com/30958501/83832125-e66fc500-a723-11ea-8599-c2348a12dc6a.jpg) | ![yolov4](https://user-images.githubusercontent.com/30958501/83832132-e96ab580-a723-11ea-9439-cf5cbbe8714d.jpg) |
