# Dockerfile
# use special python 3.7 image

FROM python:3.7-buster
MAINTAINER Jörg Weis "joerg.weis@baden.cc"
ENV REFRESHED_AT 2020-04-13

# install nginx and redirect stdout and stderr to log files
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log

RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/helloapp
COPY requirements.txt start-server.sh /opt/app/
COPY .pip_cache /opt/app/pip_cache/
COPY helloapp /opt/app/helloapp/
WORKDIR /opt/app
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
RUN chown -R www-data:www-data /opt/app
