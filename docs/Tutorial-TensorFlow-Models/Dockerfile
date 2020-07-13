FROM tensorflow/tensorflow:2.3.0-gpu

# cf. https://github.com/tensorflow/models/blob/9f9b430710273163769033660ad07715b243d269/research/object_detection/dockerfiles/tf2/Dockerfile

ENV DEBIAN_FRONTEND=noninteractive
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    wget \
    curl \
    unzip \
    gpg-agent \
    python3-cairocffi \
    protobuf-compiler \
    python3-pil \
    python3-lxml \
    python3-tk && \
    apt-get autoclean && \
    apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Install gcloud and gsutil commands
# https://cloud.google.com/sdk/docs/quickstart-debian-ubuntu
RUN CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
    export CLOUD_SDK_REPO && \
    echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    google-cloud-sdk && \
    apt-get autoclean && \
    apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Add new user to avoid running as root
RUN useradd -ms /bin/bash tensorflow
USER tensorflow

WORKDIR /home/tensorflow
# v2.3.0
RUN git clone https://github.com/tensorflow/models /home/tensorflow/models
WORKDIR /home/tensorflow/models
RUN git checkout 9f9b430710273163769033660ad07715b243d269
WORKDIR /home/tensorflow/models/research
ENV PATH="/home/tensorflow/.local/bin:${PATH}"
RUN protoc object_detection/protos/*.proto --python_out=. && \
    cp object_detection/packages/tf2/setup.py . && \
    python -m pip install --no-cache-dir --upgrade pip && \
    python -m pip install --no-cache-dir .

ENV TF_CPP_MIN_LOG_LEVEL=3

COPY .bash_aliases /root/.bash_aliases
WORKDIR /home/tensorflow/models/research/object_detection/siaizu
CMD ["/bin/bash"]
