FROM tensorflow/tensorflow:2.2.0-gpu

RUN apt-get update && apt-get install -y --no-install-recommends \
    emacs \
    build-essential \
    libsm6 \
    libxrender1 \
    libxext-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /build
ENV PIP_NO_CACHE_DIR="true"
COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r ./requirements.txt && \
    rm -rf /build

WORKDIR /src