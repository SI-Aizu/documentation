FROM python:3.8-slim-buster

RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir tensorflow==2.2.0

WORKDIR /logs
ENTRYPOINT ["tensorboard", "--logdir", "/logs"]
