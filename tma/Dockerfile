FROM node:18-alpine

WORKDIR /app

# Копирование package.json и установка зависимостей
COPY package*.json ./
RUN npm ci --only=production

# Копирование исходного кода
COPY . .

# Сборка приложения
RUN npm run build

# Установка сервера для статических файлов
RUN npm install -g serve

# Экспорт порта
EXPOSE 3000

# Запуск приложения
CMD ["serve", "-s", "dist", "-l", "3000"]