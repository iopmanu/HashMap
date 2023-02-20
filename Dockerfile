FROM python:3.8-alpine

LABEL "project"="HashTable"
LABEL "creator"="iopmanu"

RUN apk add --no-cache --virtual .build-deps \
    build-base openssl-dev libffi-dev


RUN pip install --upgrade pip
RUN pip install pytest

COPY . /project

WORKDIR "/project"

CMD pytest -s -v linked_list_tests.py
