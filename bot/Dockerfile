FROM python:3.10.8-slim-buster

WORKDIR /usr/src/app

# No .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Output sent to terminal directly
ENV  PYTHONUNBUFFERED 1
ENV TZ=Asia/Hong_Kong


RUN apt-get update
RUN echo "Y" | apt install build-essential

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app