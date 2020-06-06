FROM tensorflow/tensorflow:2.2.0-gpu

RUN apt-get update && apt-get install -y --no-install-recommends \
    emacs \
    build-essential \
    libsm6 \
    libxrender1 \
    libxext-dev &&\
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install \
    matplotlib \
    seaborn \
    pandas \
    opencv-python \
    sklearn \
    pydot

WORKDIR /src
