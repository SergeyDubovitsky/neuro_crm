FROM python:3.12-alpine

COPY manage.py requirements.txt neuro_crm/* /app/
WORKDIR /app

RUN pip install -U pip && pip install uv && uv pip install --system -r requirements.txt
