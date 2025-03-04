FROM python:3.12.7-alpine3.20

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /src
COPY ./src /src

RUN adduser -D user
USER user
