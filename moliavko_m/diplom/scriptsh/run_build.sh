#!/bin/bash

docker build . -t api-tests  # Собираем Docker-образ с тегом api-tests
docker run -v "$(pwd)"/report:/opt/api/report api-tests  # Запускаем контейнер, монтируя директорию для сохранения отчета

