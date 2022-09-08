FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get -y install python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt