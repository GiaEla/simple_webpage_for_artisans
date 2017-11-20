#
# Django dockerfile, please link code to /usr/src/app
#

FROM python:3.5

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/
RUN pip install --no-cache-dir -r /usr/src/requirements.txt
RUN pip install uwsgi

ADD dist.tar.gz /usr/src/app
#COPY uwsgi.ini /usr/src/app/uwsgi.ini
#COPY prod_run.sh /usr/src/app/prod_run.sh

WORKDIR /usr/src/app

RUN chmod +x /usr/src/app/prod_run.sh
RUN chmod +x /usr/src/app/manage.py

ENTRYPOINT /usr/src/app/prod_run.sh