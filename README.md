# Telegram Bot + TMA App Monorepo

Монорепозиторий для Telegram бота на Python и Telegram Mini App на React.

## Структура проекта

- `bot/`
- `api/`
- `tma/` 
- `docker-compose.yml`
- `setup.sh`

## Docker

1. docker compose

   ```bash
   # Полная очистка Docker Compose окружения
   docker compose down -v --rmi all

   # Удаление неиспользуемых данных Docker
   docker system prune -a -f --volumes

   # Перезапуск tma
   docker compose build --no-cache tma && docker compose up

   # Перезапуск api/bot
   docker compose build api && docker compose up
   docker compose build bot && docker compose up

   # Перезапуск всего
   docker compose build api && docker compose build bot && docker compose build --no-cache tma && docker compose up
   ```


## Быстрый старт

### 1. Подготовка сервера

sudo ./setup.sh