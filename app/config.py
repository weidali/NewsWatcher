import os

# --- Основные настройки ---

# Проверка и создание папки logs/
os.makedirs('logs', exist_ok=True)

# RSS-ленты
RSS_FEEDS = [
    "https://news.google.com/rss?hl=en",
    "https://www.reutersagency.com/feed/?best-sectors=political-general&post_type=best"
]

# Ключевые слова и их переводы
KEYWORDS_MAPPING = {
    'crisis': 'кризис',
    'inflation': 'инфляция',
    'war': 'война',
    'conflict': 'конфликт',
    'cyberattack': 'кибератака',
    'pandemic': 'пандемия',
    'climate': 'климат',
    'bitcoin': 'биткоин',
    'cryptocurrency': 'криптовалюта',
    'banking': 'банковская система',
    'recession': 'рецессия'
}

# Ключевые слова
KEYWORDS = list(KEYWORDS_MAPPING.keys())

# Telegram настройки
BOT_TOKEN = 'ТВОЙ_BOT_TOKEN'
CHAT_ID = 'ТВОЙ_CHAT_ID'

# Порог роста (%) для уведомлений
GROWTH_THRESHOLD = 30

# Файл с данными вчерашнего дня
YESTERDAY_FILE = "yesterday_counts.json"
