import os
import logging
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from config import BOT_TOKEN

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Создание экземпляра бота
bot = telebot.TeleBot(BOT_TOKEN)

# Создание клавиатуры
def create_main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('ℹ️ Помощь'))
    keyboard.add(KeyboardButton('👋 Привет'), KeyboardButton('🔄 Повтори'))
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
    logger.info(f"Новый пользователь: {user.first_name} (ID: {user.id})")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    help_text = """
🤖 *Доступные команды:*

*/start* - Начать работу
*/help* - Показать справку

*Кнопки:*
👋 *Привет* - Поприветствовать
🔄 *Повтори* - Повторить последнее сообщение
ℹ️ *Помощь* - Показать эту справку

*Также ты можешь:*
📝 Отправить любое сообщение - я его повторю
🕒 Отправить время - покажу текущее время
    """
    bot.send_message(
        message.chat.id,
        help_text,
        parse_mode='Markdown',
        reply_markup=create_main_keyboard()
    )

# Обработчик кнопки "Привет"
@bot.message_handler(func=lambda message: message.text == '👋 Привет')
def handle_hello(message):
    user = message.from_user
    bot.send_message(
        message.chat.id,
        f"И тебе привет, {user.first_name}! 😊\nКак твои дела?",
        reply_markup=create_main_keyboard()
    )

# Обработчик кнопки "Помощь"
@bot.message_handler(func=lambda message: message.text == 'ℹ️ Помощь')
def handle_help_button(message):
    handle_help(message)

# Обработчик кнопки "Повтори"
@bot.message_handler(func=lambda message: message.text == '🔄 Повтори')
def handle_repeat_last(message):
    bot.send_message(
        message.chat.id,
        "Отправь мне сообщение, и я его повторю! 📝",
        reply_markup=create_main_keyboard()
    )

# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_text(message):
    user_text = message.text
    
    # Проверяем, не является ли сообщение командой с клавиатуры
    if user_text in ['👋 Привет', 'ℹ️ Помощь', '🔄 Повтори']:
        return  # Эти сообщения уже обрабатываются другими хендлерами
    
    response = f"🔁 Ты сказал: *{user_text}*"
    
    bot.send_message(
        message.chat.id,
        response,
        parse_mode='Markdown',
        reply_markup=create_main_keyboard()
    )
    
    logger.info(f"Пользователь {message.from_user.id} отправил: {user_text}")

# Обработчик всех остальных типов сообщений
@bot.message_handler(content_types=['photo', 'document', 'sticker', 'voice'])
def handle_other_messages(message):
    bot.send_message(
        message.chat.id,
        "Круто! Но я пока умею работать только с текстом 📝",
        reply_markup=create_main_keyboard()
    )

# Вебхук обработчики (если используется вебхук)
@bot.message_handler(commands=['set_webhook'])
def set_webhook(message):
    if message.from_user.id != YOUR_ADMIN_USER_ID:  # Замените на ваш ID
        bot.reply_to(message, "У вас нет прав для этой команды.")
        return
    
    from config import WEBHOOK_URL, WEBHOOK_PATH
    if WEBHOOK_URL:
        bot.set_webhook(url=f"{WEBHOOK_URL}{WEBHOOK_PATH}")
        bot.reply_to(message, f"Вебхук установлен: {WEBHOOK_URL}{WEBHOOK_PATH}")
    else:
        bot.reply_to(message, "WEBHOOK_URL не настроен в конфигурации")

@bot.message_handler(commands=['remove_webhook'])
def remove_webhook(message):
    if message.from_user.id != YOUR_ADMIN_USER_ID:  # Замените на ваш ID
        bot.reply_to(message, "У вас нет прав для этой команды.")
        return
    
    bot.remove_webhook()
    bot.reply_to(message, "Вебхук удален, используется polling")

# Функция для запуска через вебхук
def run_webhook():
    from config import WEBHOOK_URL, WEBHOOK_PATH, PORT
    if WEBHOOK_URL:
        bot.remove_webhook()
        bot.set_webhook(url=f"{WEBHOOK_URL}{WEBHOOK_PATH}")
        logger.info(f"Вебхук установлен: {WEBHOOK_URL}{WEBHOOK_PATH}")
    else:
        logger.info("WEBHOOK_URL не настроен, используется polling")

# Основная функция запуска
def main():
    try:
        logger.info("Запуск бота...")
        
        # Проверяем, используем ли мы вебхук или polling
        from config import WEBHOOK_URL, PORT
        
        if WEBHOOK_URL:
            # Для вебхука нужен сервер (например, Flask)
            run_webhook()
        else:
            # Запускаем polling
            logger.info("Используется polling режим")
            bot.infinity_polling(timeout=60, long_polling_timeout=60)
            
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")
        raise

if __name__ == '__main__':
    main()