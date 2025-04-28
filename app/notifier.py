from telegram import Bot
from app import config

def send_telegram_message(message):
    """
    Отправляет сообщение в Telegram
    """
    bot = Bot(token=config.BOT_TOKEN)
    bot.send_message(chat_id=config.CHAT_ID, text=message)
