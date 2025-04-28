import feedparser
from collections import Counter
from telegram import Bot
import json
import os
import logging
import sys
from app import parser, analyzer

# --- Настройки ---

# Проверка и создание папки logs/
os.makedirs('logs', exist_ok=True)

# Настройка логирования
logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# RSS-ленты новостей (можно дополнять)
RSS_FEEDS = [
    "https://news.google.com/rss?hl=en",
    "https://www.reutersagency.com/feed/?best-sectors=political-general&post_type=best"
]

# Ключевые темы для отслеживания
KEYWORDS = [
    'crisis', 'inflation', 'war', 'conflict', 'cyberattack', 'pandemic',
    'climate', 'bitcoin', 'cryptocurrency', 'banking', 'recession'
]

# Telegram настройки
BOT_TOKEN = 'ТВОЙ_BOT_TOKEN'
CHAT_ID = 'ТВОЙ_CHAT_ID'

# Порог роста упоминаний темы (%) для сигнала
GROWTH_THRESHOLD = 30

# Файл для хранения вчерашних подсчетов
YESTERDAY_FILE = "yesterday_counts.json"

# --- Функции ---

def send_telegram_message(message):
    bot = Bot(token=BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message)

def fetch_news():
    all_text = ""
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            all_text += " " + entry.title + " " + entry.description
    return all_text.lower()

def analyze_text(text):
    word_counts = Counter()
    for keyword in KEYWORDS:
        word_counts[keyword] = text.count(keyword.lower())
    return word_counts

def load_yesterday_counts():
    if os.path.exists(YESTERDAY_FILE):
        with open(YESTERDAY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_today_counts(counts):
    with open(YESTERDAY_FILE, "w") as f:
        json.dump(counts, f)

def compare_and_alert(today_counts, yesterday_counts):
    for word, today_count in today_counts.items():
        yesterday_count = yesterday_counts.get(word, 0)
        
        if yesterday_count == 0:
            continue

        growth = ((today_count - yesterday_count) / yesterday_count) * 100

        if growth > GROWTH_THRESHOLD:
            message = f"🚨 Всплеск темы: '{word}' вырос на {growth:.1f}% по сравнению со вчерашним днем!"
            print(message)
            send_telegram_message(message)

# --- Основной процесс ---

def main():
    print("🚀 Старт анализа новостей...")
    logging.info("🚀 Запуск News Watcher...")
    
    text = fetch_news()
    today_counts = analyze_text(text)
    yesterday_counts = load_yesterday_counts()

    print("\n📊 Сегодняшние упоминания тем:")
    for word, count in today_counts.items():
        print(f"{word}: {count}")

    compare_and_alert(today_counts, yesterday_counts)
    save_today_counts(today_counts)

    print("\n✅ Завершено.")

if __name__ == "__main__":
    main()
