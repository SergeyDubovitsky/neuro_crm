FROM python:3.12-alpine

COPY . /app
WORKDIR /app

RUN pip intall -U pip && pip install -r requirements.txt
