FROM python:3.4.3


RUN mkdir -p /app

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD uwsgi --ini /app/webapp2/wsgi.ini

EXPOSE 9090