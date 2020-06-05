FROM nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES utility,compute
ENV CUDA_HOME="/usr/local/cuda-10.2"
ENV LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${CUDA_HOME}/lib64
SHELL ["/bin/bash", "-c"]

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    tzdata \
    apt-utils \
    emacs \
    vim \
    git \
    wget \
    gnupg2 \
    ca-certificates \
    build-essential \
    libopencv-dev \
    python3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /src
COPY Makefile /src/Makefile
COPY yolov4_weights.sh /src/yolov4_weights.sh
RUN git clone --depth=1 https://github.com/AlexeyAB/darknet.git -b darknet_yolo_v4_pre
WORKDIR /src/darknet
RUN wget --quiet https://pjreddie.com/media/files/yolov3.weights && \
    bash yolov4_weights.sh && \
    make -j8
