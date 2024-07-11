FROM python:3.12

RUN apt-get update && apt-get install -y

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip && python -m pip install -r requirements.txt

COPY . .
