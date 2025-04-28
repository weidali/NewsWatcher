from collections import Counter
from app import config
import logging

def analyze_text(text):
    """
    Анализирует текст и подсчитывает упоминания ключевых слов
    """
    word_counts = Counter()
    for keyword in config.KEYWORDS:
        word_counts[keyword] = text.count(keyword.lower())
    return word_counts
