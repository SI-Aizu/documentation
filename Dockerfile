FROM python:3.6.9-slim-stretch

WORKDIR /build
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential
COPY requirements.txt requirements.txt
RUN pip install -r ./requirements.txt && \
    pip install black
WORKDIR /src
