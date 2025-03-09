# WhisperWave_Queue

## Pre-requisites
In order to run WhisperWave Queue you need to have RabbitMQ installed on your machine. If you choose to run it in a docker container, you can install docker desktop or podman.

We recomend the use of docker desktop
To install docker desktop follow the link: https://www.docker.com/products/docker-desktop/


## Running WhisperWave on Docker
In to run whisperwave in docker containers we've conviniently added a docker-compose file. To run the docker compose file run the following command in the folder where you clone the project:

This docker compose it also create another container for RabbitMQ.

Open your terminal application;

```
docker-compose up -d
```

To check the running container run the following command on your terminal application.

```
docker ps
```
