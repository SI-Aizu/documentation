FROM tensorflow/tensorflow:2.3.0-gpu

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
    apt-get clean && \
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
