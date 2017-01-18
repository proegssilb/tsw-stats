FROM alpine:3.5
MAINTAINER David Bliss <minifig404@gmail.com>

RUN apk update && apk add python3 py3-psycopg2

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN mkdir db pages static views

COPY requirements.txt main.py setup.py /usr/src/app/

RUN pip3 install -r requirements.txt

COPY static /usr/src/app/static/
COPY views /usr/src/app/views/
COPY db /usr/src/app/db/
COPY pages /usr/src/app/pages/

EXPOSE 8080

CMD [ "python3", "./main.py" ]
