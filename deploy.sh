#!/bin/bash

set -e

echo "🚀 Запуск деплоя Telegram Bot + TMA App..."

# Проверка наличия .env файла
if [ ! -f .env ]; then
    echo "❌ Файл .env не найден. Создайте его на основе .env.example"
    exit 1
fi

# Загрузка переменных окружения
source .env

# Проверка обязательных переменных
if [ -z "$BOT_TOKEN" ]; then
    echo "❌ Переменная BOT_TOKEN не установлена в .env файле"
    exit 1
fi

# Остановка существующих контейнеров
echo "🛑 Остановка существующих контейнеров..."
docker-compose down || true

# Сборка и запуск контейнеров
echo "🐳 Сборка и запуск контейнеров..."
docker-compose up --build -d

# Ожидание запуска сервисов
echo "⏳ Ожидание запуска сервисов..."
sleep 30

# Проверка здоровья сервисов
echo "🔍 Проверка здоровья сервисов..."

# Проверка nginx
if curl -f http://localhost/health > /dev/null 2>&1; then
    echo "✅ Nginx работает корректно"
else
    echo "❌ Nginx не отвечает"
    docker-compose logs nginx
    exit 1
fi

# Проверка TMA приложения
if curl -f http://localhost:3000 > /dev/null 2>&1; then
    echo "✅ TMA приложение работает корректно"
else
    echo "⚠️  TMA приложение может быть недоступно"
fi

# Логи бота для проверки
echo "📋 Логи бота:"
docker-compose logs bot --tail=20

echo ""
echo "🎉 Деплой завершен успешно!"
echo ""
echo "🌐 Доступные сервисы:"
echo "   - TMA App: http://your-server-ip"
echo "   - Nginx: http://localhost"
echo ""
echo "📝 Для просмотра логов используйте:"
echo "   docker-compose logs -f bot    # Логи бота"
echo "   docker-compose logs -f tma    # Логи TMA приложения"
echo "   docker-compose logs -f nginx  # Логи nginx"