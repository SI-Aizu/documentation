FROM nvidia/cuda:10.2-base-ubuntu18.04

ENV DEBIAN_FRONTEND=noninteractive
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES utility,compute
ENV CUDA_HOME="/usr/local/cuda-10.2"
ENV LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${CUDA_HOME}/lib64

SHELL ["/bin/bash", "-c"]

RUN apt-get update && \
    apt-get -y install --no-install-recommends \
    git \
    wget \
    curl \
    unzip \
    build-essential \
    libsm6 libxext6 libxrender-dev && \
    rm -rf /var/lib/apt/lists/*

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    mkdir ~/.conda && \
    bash ~/miniconda.sh -b -p "${HOME}/miniconda" && \
    rm ~/miniconda.sh && \
    ln -s ~/miniconda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". ~/miniconda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    eval "$(~/miniconda/bin/conda shell.bash hook)" && \
    conda update -n base -c defaults conda -y && \
    echo "conda activate conda" >> ~/.bashrc

WORKDIR /root/protoc
RUN wget --quiet -O protobuf.zip https://github.com/protocolbuffers/protobuf/releases/download/v3.9.1/protoc-3.9.1-linux-x86_64.zip
RUN unzip -o ./protobuf.zip
RUN mv ./bin/protoc /usr/local/bin/
WORKDIR /root
RUN rm -rf ./protoc

RUN git clone --depth 1 https://github.com/tensorflow/models -b v1.13.0
WORKDIR /root/models/research
RUN /usr/local/bin/protoc object_detection/protos/*.proto --python_out=.

WORKDIR /root/build
COPY conda.yml ./conda.yml
# https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md
RUN eval "$(~/miniconda/bin/conda shell.bash hook)" && \
    conda env create -f ./conda.yml

RUN git clone https://github.com/cocodataset/cocoapi.git
WORKDIR /root/build/cocoapi/
RUN git checkout 636becdc73d54283b3aac6d4ec363cffbb6f9b20
WORKDIR /root/build/cocoapi/PythonAPI
RUN eval "$(~/miniconda/bin/conda shell.bash hook)" && \
    conda activate conda && \
    make && \
    python3 -m pip install --no-cache-dir pycocotools==2.0.0

COPY .bash_aliases /root/.bash_aliases
WORKDIR /root/models/research/object_detection_tools
ENTRYPOINT ["/bin/bash"]
