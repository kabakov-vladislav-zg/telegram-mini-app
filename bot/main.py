import telebot
from telebot.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import os
from urllib.parse import urlencode

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

# Обработчик кнопки "Анкета"
@bot.message_handler(func=lambda message: message.text == '👋 Анкета')
def handle_hello(message):
    app_url = "https://vladiksfriendsprofilebot.webtm.ru"
    user = message.from_user
    chat = message.chat
    text = f"""
      👋 Привет
      Заполни анкету друга для {user.first_name}
    """
    params = {
      'chat': chat,
      'user': user,
    }
    url = f"{app_url}?{urlencode(params, doseq=True)}"

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