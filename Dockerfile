FROM python:3.8-slim-buster

ENV DEBIAN_FRONTEND=noninteractive
ENV PIP_NO_CACHE_DIR="true"

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    wget \
    vim && \
    apt-get autoclean && \
    apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /build
COPY ./dev/requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r ./requirements.txt && \
    python3 -m pip check && \
    rm -rf /build

WORKDIR /src
