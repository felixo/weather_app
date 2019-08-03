#!/usr/bin/env bash
docker pull rogunborn/docker_weather:latest
docker run -ti --rm --name weather -v $PWD:/usr/local/weather -p 8081:8081 rogunborn/docker_weather /bin/bash -c "cd /usr/local/weather; python3 weather_app/manage.py migrate; python3 weather_app/manage.py runserver 0.0.0.0:8081 "