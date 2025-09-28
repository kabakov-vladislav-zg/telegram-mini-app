#!/bin/bash

set -e

echo "🚀 Начало настройки сервера и установки зависимостей..."

# Проверка прав суперпользователя
if [ "$EUID" -ne 0 ]; then
    echo "❌ Пожалуйста, запустите скрипт с правами root: sudo ./setup.sh"
    exit 1
fi

# Обновление системы
echo "📦 Обновление пакетов системы..."
apt-get update
apt-get upgrade -y

# Установка Docker
if ! command -v docker &> /dev/null; then
    echo "🐳 Установка Docker..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    rm get-docker.sh
fi

# Установка Docker Compose
if ! command -v docker-compose &> /dev/null; then
    echo "🐳 Установка Docker Compose..."
    curl -L "https://github.com/docker/compose/releases/download/v2.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
fi

# Добавление пользователя в группу docker
if ! groups $SUDO_USER | grep &>/dev/null '\bdocker\b'; then
    echo "👥 Добавление пользователя $SUDO_USER в группу docker..."
    usermod -aG docker $SUDO_USER
fi

# Создание необходимых директорий
echo "📁 Создание структуры директорий..."
mkdir -p /var/log/telegram-app
mkdir -p /opt/telegram-app

# Настройка firewall
echo "🔥 Настройка firewall..."
if command -v ufw &> /dev/null; then
    ufw allow 80/tcp
    ufw allow 443/tcp
    ufw allow 22/tcp
    ufw --force enable
fi

# Установка системных зависимостей
echo "📚 Установка системных зависимостей..."
apt-get install -y \
    curl \
    wget \
    git \
    python3 \
    python3-pip \
    nodejs \
    npm

# Копирование файлов проекта
echo "📄 Копирование файлов проекта..."
cp -r . /opt/telegram-app/
chown -R $SUDO_USER:$SUDO_USER /opt/telegram-app

echo "✅ Настройка сервера завершена!"
echo ""
echo "📝 Следующие шаги:"
echo "1. Перейдите в директорию проекта: cd /opt/telegram-app"
echo "2. Настройте переменные окружения в файле .env"
echo "3. Запустите деплой: ./deploy.sh"
echo ""
echo "⚠️  Не забудьте перезапустить сессию или выполнить: newgrp docker"