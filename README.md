# Telegram Bot + TMA App Monorepo

Монорепозиторий для Telegram бота на Python и Telegram Mini App на React.

## Структура проекта

- `bot/` - Python бот без базы данных
- `tma/` - React TMA приложение
- `nginx/` - Конфигурация nginx
- `docker-compose.yml` - Docker Compose конфигурация
- `setup.sh` - Скрипт настройки сервера
- `deploy.sh` - Скрипт деплоя

## Быстрый старт

### 1. Подготовка сервера

```bash
chmod +x setup.sh deploy.sh
sudo ./setup.sh