#3.9.4
FROM python:3

LABEL maintainer="Phong Tran"

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY . /app