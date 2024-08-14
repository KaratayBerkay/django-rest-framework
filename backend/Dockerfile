FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app

COPY requirements.txt /app/requirements.txt
COPY docker-entrypoint.sh /app/docker-entrypoint.sh

WORKDIR /app

ADD .. /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

RUN chmod +x /app/docker-entrypoint.sh