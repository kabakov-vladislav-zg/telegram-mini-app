import os

# Токен бота (должен быть установлен в переменных окружения)
BOT_TOKEN = os.getenv('BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')

# Настройки вебхука (если используется)
WEBHOOK_URL = os.getenv('WEBHOOK_URL', '')
WEBHOOK_PATH = os.getenv('WEBHOOK_PATH', '/webhook')

# Порт для сервера
PORT = int(os.getenv('PORT', 8080))

# ID администратора (для специальных команд)
ADMIN_USER_ID = int(os.getenv('ADMIN_USER_ID', '0'))