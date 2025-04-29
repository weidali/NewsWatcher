import os

# --- Основные настройки ---

# Проверка и создание папки logs/
os.makedirs('logs', exist_ok=True)

# RSS-ленты
RSS_FEEDS = [
    "https://news.google.com/rss?hl=en",  # Google News (общая лента)
    "https://www.reutersagency.com/feed/?best-sectors=political-general&post_type=best"
    "https://feeds.a.dj.com/rss/RSSWorldNews.xml",  # Wall Street Journal - мировые новости
    "https://www.ft.com/?format=rss",  # Financial Times (общая лента)
    "https://www.bloomberg.com/feed/podcast/etf-report.xml",  # Bloomberg - отчёты ETF
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",  # New York Times - мировые новости
    "https://feeds.reuters.com/Reuters/worldNews",  # Reuters - мировые новости
    "https://feeds.bbci.co.uk/news/world/rss.xml",  # BBC News - мировые новости
    "https://www.aljazeera.com/xml/rss/all.xml",  # Al Jazeera - все новости
    "https://feeds.arstechnica.com/arstechnica/index",  # Ars Technica (в том числе технологии)
    "https://www.cnbc.com/id/100003114/device/rss/rss.html",  # CNBC - топ новости
    "https://www.marketwatch.com/rss/topstories",  # MarketWatch - топ истории
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
