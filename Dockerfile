FROM python:3.9-slim-buster

COPY httpservice.py /app/httpservice.py

RUN apt-get update && \
    apt-get install -y netcat && \
    pip install --no-cache-dir Flask

WORKDIR /app

EXPOSE 8080

CMD python httpservice.py