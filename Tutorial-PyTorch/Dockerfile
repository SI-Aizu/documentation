FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-runtime

ENV DEBIAN_FRONTEND=noninteractive
ENV PIP_NO_CACHE_DIR="true"

WORKDIR /build
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    wget \
    vim \
    libopencv-dev \
    software-properties-common && \
    curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y --no-install-recommends nodejs && \
    apt-get autoclean && \
    apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade pip \
    jupyterlab matplotlib ipywidgets \
    opencv-contrib-python-headless opencv-python-headless && \
    python3 -m pip check && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager && \
    rm -rf /build

WORKDIR /src
