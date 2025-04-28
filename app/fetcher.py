import feedparser
from app import config

def fetch_news():
    """
    Загружает текст новостей из всех RSS-лент
    """
    all_text = ""
    for url in config.RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            all_text += " " + entry.title + " " + entry.description
    return all_text.lower()
