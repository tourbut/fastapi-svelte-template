# Stage 1: Build the React app
FROM node:20 AS build

WORKDIR /app

COPY ./frontend .

RUN npm install
RUN npm run build

# Stage 2: Serve the app from Nginx
FROM nginx:latest

LABEL maintainer="Knowslog <Knowslog01@gmail.com>"

RUN apt-get install tzdata

RUN apt-get update && \
    apt-get install -y gettext-base && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the build output to replace the default nginx contents.
COPY --from=build /app/build /usr/share/nginx/html

COPY ./frontend/nginx/nginx.conf.template /etc/nginx/nginx.conf.template
COPY ./frontend/nginx/conf.sh /conf.sh