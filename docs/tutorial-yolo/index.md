# YOLO v3 and v4

```console
$ nvidia-smi
NVIDIA-SMI 440.82       Driver Version: 440.82       CUDA Version: 10.2
```

`nvidia-smi` で確認できる CUDA Version と Base Docker image `nvidia/cuda` の tag を一致させる。

```sh
sudo docker build . -t darknet-yolo:latest --build-arg BASE_IMAGE="nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04"
```
