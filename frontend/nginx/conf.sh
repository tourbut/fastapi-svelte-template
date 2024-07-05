#!/bin/bash

echo "Configuring nginx"
# envsubst를 사용하여 환경 변수로 nginx.conf.template 파일을 처리하고 결과를 /etc/nginx/nginx.conf에 저장
envsubst '$DOMAIN' < /etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf
