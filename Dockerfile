FROM ubuntu:latest

RUN apt-get update

RUN apt-get install python3.8 -y

WORKDIR /code

COPY src .

RUN apt-get install python3-pip -y

RUN pip3 install -r requirements.txt

ENV FLASK_APP=main:create_app

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "main:create_app()"]