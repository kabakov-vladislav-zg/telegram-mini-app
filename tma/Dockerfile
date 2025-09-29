FROM node:18-alpine AS builder

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем package.json и package-lock.json
COPY package*.json ./

# Устанавливаем зависимости
RUN npm ic

# Копируем весь код приложения в контейнер
COPY . .

# Собираем статический сайт для продакшена
RUN npm run build:web

# --- Этап 2: Развертывание с помощью Nginx ---
# Используем легковесный образ Nginx
FROM nginx:stable-alpine

# Копируем статические файлы из этапа сборки (из каталога /app/dist) в директорию Nginx для статики
COPY --from=builder /app/dist /usr/share/nginx/html

# Копируем кастомный файл конфигурации Nginx (опционально, если требуется)
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# Открываем порт, который слушает Nginx (по умолчанию 80)
EXPOSE 80

# Запускаем Nginx
CMD ["nginx", "-g", "daemon off;"]