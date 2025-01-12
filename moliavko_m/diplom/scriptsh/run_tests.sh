#!/bin/bash

npm install newman newman-reporter-htmlextra  # Устанавливаем newman и newman-reporter-htmlextra

if ! [ -d ./report/ ]; then  # Проверяем наличие директории для отчетов
  mkdir report
fi

npm test  # Запускаем тесты с помощью скрипта test из package.json

