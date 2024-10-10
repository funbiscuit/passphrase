FROM python:3.12-slim

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /app

COPY . .

ENTRYPOINT ["python", "./generate.py"]
