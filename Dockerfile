FROM python:3.7.9

LABEL maintainer="Phong Tran"

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY ./requirements.txt /requirements.txt
COPY ./.env /app/.env
RUN pip install -r /requirements.txt

COPY . /app