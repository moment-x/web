FROM python:3.4.3

RUN apt-get -y update
RUN apt-get -y upgrade

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install -r requirements.txt

CMD uwsgi --ini /usr/src/app/webapp2/webapp2/wsgi.ini

EXPOSE 9090