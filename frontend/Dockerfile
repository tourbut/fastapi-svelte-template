FROM nginx:latest

LABEL maintainer="Knowslog <Knowslog01@gmail.com>"

RUN apt-get install tzdata

RUN apt-get update && \
    apt-get install -y gettext-base && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./frontend/nginx/nginx.conf.template /etc/nginx/nginx.conf.template
COPY ./frontend/nginx/conf.sh /conf.sh
RUN chmod +x /conf.sh