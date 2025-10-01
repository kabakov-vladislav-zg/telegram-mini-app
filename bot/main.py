import telebot
from telebot.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import os
from urllib.parse import urlencode
import json
import base64

# Создание экземпляра бота
bot = telebot.TeleBot(os.getenv('BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE'))

# Создание клавиатуры
def create_main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('👋 Анкета'), KeyboardButton('ℹ️ Помощь'))
    return keyboard

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    user = message.from_user
    welcome_text = (
        f"Привет, {user.first_name}! 👋\n"
        f"Я простой бот на pytelegrambotapi.\n"
        f"Выбери действие на клавиатуре или отправь мне сообщение!"
    )
    
    bot.send_message(
        message.chat.id,
        welcome_text,
        reply_markup=create_main_keyboard()
    )

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    help_text = """
      🤖 *Доступные команды:*

      */start* - Начать работу
      */help* - Показать справку

      *Кнопки:*
      👋 *Привет* - Поприветствовать
      ℹ️ *Помощь* - Показать эту справку
    """
    bot.send_message(
        message.chat.id,
        help_text,
        parse_mode='Markdown',
        reply_markup=create_main_keyboard()
    )

def encode_compact(data_dict):  
  json_str = json.dumps(data_dict, separators=(',', ':'))
  base64_encoded = base64.b64encode(json_str.encode('utf-8')).decode('utf-8')
  
  return (
    base64_encoded
    .replace('+', '-')
    .replace('/', '_')
    .replace('=', '')
  )

# Обработчик кнопки "Анкета"
@bot.message_handler(func=lambda message: message.text == '👋 Анкета')
def handle_hello(message):
    app_url = "https://vladiksfriendsprofilebot.webtm.ru"
    user = message.from_user
    chat = message.chat
    text = f"""👋 Привет
Заполни анкету друга для {user.first_name}
"""
    attach_data = {
      'id': user.id,
      'is_bot': user.is_bot,
      'first_name': user.first_name,
      'last_name': user.last_name,
      'username': user.username,
      'language_code': user.language_code
    }
    attach_string = encode_compact(attach_data)
    url = f"{app_url}?startattach={attach_string}"

    keyboard = [[InlineKeyboardButton(
      "Анкета",
      web_app=WebAppInfo(url=url))
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.send_message(
      chat.id,
      text,
      reply_markup=reply_markup
    )

# Обработчик кнопки "Помощь"
@bot.message_handler(func=lambda message: message.text == 'ℹ️ Помощь')
def handle_help_button(message):
    handle_help(message)

    
# Обработчик всех остальных типов сообщений
@bot.message_handler(content_types=['photo', 'document', 'sticker', 'voice'])
def handle_other_messages(message):
    bot.send_message(
        message.chat.id,
        "Круто! Но я пока умею работать только с текстом 📝",
        reply_markup=create_main_keyboard()
    )

# Основная функция запуска
def main():
    try:                
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
            
    except Exception as e:
        raise

if __name__ == '__main__':
    main()