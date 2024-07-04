#! /usr/bin/env sh 

echo "Docker Container Down"

sudo docker compose -f "docker-compose.yaml" down 

echo "Docker Build & Up"

sudo docker compose -f "docker-compose.yaml" up -d --build

echo "Docker None Images Remove"

sudo docker rmi $(sudo docker images -f "dangling=true" -q)