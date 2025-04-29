import asyncio
from telegram import Bot
from app import config

async def send_telegram_message(message):
    """
    Отправляет сообщение в Telegram
    """
    bot = Bot(token=config.BOT_TOKEN)
    await bot.send_message(chat_id=config.CHAT_ID, text=message)

def notify(message):
    asyncio.run(send_telegram_message(message))

def send_error_notification(error_message):
    error_text = f"❗ Ошибка в News Watcher:\n{error_message}"
    notify(error_text)
