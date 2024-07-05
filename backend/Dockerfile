FROM tiangolo/uvicorn-gunicorn:python3.11-slim

WORKDIR /app/

LABEL maintainer="scshin88 <scshin88@gmail.com>"

RUN apt-get install tzdata
COPY ./backend/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./backend/config/gunicorn_conf.py /app/gunicorn_conf.py

COPY ./backend/start.sh /app/
RUN chmod +x /app/start.sh