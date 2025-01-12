# Используем образ Node.js
FROM node:22

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /opt/api/

# Копируем package.json и package-lock.json для установки зависимостей
COPY package.json ./ package-lock.json ./


# Устанавливаем зависимости проекта
RUN yarn install


# Копируем все остальные файлы проекта внутрь контейнера
COPY . .

# Запускаем run_tests.sh при запуске контейнера
CMD ["./run_tests.sh"]
