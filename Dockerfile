FROM ubuntu:latest
RUN apt-get update
RUN apt install -qy software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt -qy install python3.7
RUN apt install -qy python3-pip
RUN apt-get -qy install mysql-server
WORKDIR /app
COPY . /app
RUN /bin/sh -c 'service mysql start;mysql <"new.sql"'
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD python3 app1.py
