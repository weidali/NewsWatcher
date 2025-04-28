import logging

def analyze(news_list):
    """
    Базовый анализатор новостей.
    Сейчас просто ищет частотность ключевых слов.
    """

    logging.info("Начало анализа новостей...")

    keywords = ["кризис", "искусственный интеллект", "саммит", "рост", "авария"]
    results = {}

    for news in news_list:
        for keyword in keywords:
            if keyword.lower() in news.lower():
                results.setdefault(keyword, []).append(news)

    logging.info(f"Ключевых тем найдено: {len(results)}")
    return results
