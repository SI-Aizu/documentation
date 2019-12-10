FROM python:3.6.9-slim-stretch

WORKDIR /build
RUN apt-get update
COPY requirements.txt requirements.txt
RUN pip install -r ./requirements.txt
WORKDIR /src

