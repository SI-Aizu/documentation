FROM tensorflow/tensorflow:2.3.0-gpu

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    vim \
    emacs \
    build-essential \
    libsm6 \
    libxrender1 \
    libxext-dev \
    libcairo2-dev \
    libgirepository1.0-dev \
    python3-gi \
    python3-gi-cairo \
    gir1.2-gtk-3.0 \
    pkg-config \
    python3-dev && \
    apt-get autoclean && \
    apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*
# hadolint ignore=DL3015
RUN apt-get update && apt-get install -y libopencv-dev && \
    apt-get autoclean && \
    apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /build
ENV PIP_NO_CACHE_DIR="true"
COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --ignore-installed pycairo pyxdg pygobject && \
    python3 -m pip install -r ./requirements.txt && \
    python3 -m pip check && \
    rm -rf /build

WORKDIR /src
