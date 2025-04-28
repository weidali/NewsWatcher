import sys
import time
import tracemalloc
from app import fetcher, analyzer, notifier, storage, config, logger

# Настройка логгирования
log = logger.setup_logger()

def compare_and_alert(today_counts, yesterday_counts):
    for word, today_count in today_counts.items():
        yesterday_count = yesterday_counts.get(word, 0)
        
        if yesterday_count == 0:
            continue

        growth = ((today_count - yesterday_count) / yesterday_count) * 100

        if growth > config.GROWTH_THRESHOLD:
            r_word = config.KEYWORDS_MAPPING.get(word, word)
            message = f"🚨 Всплеск темы: '{r_word}' вырос на {growth:.1f}%!"
            print(message)
            notifier.send_telegram_message(message)

def main():
    print("🚀 Старт анализа новостей...")
    log.info("🚀 Запуск News Watcher...")

    start_time = time.time()  # Засекаем время
    tracemalloc.start()       # Старт отслеживания памяти

    try:
        text = fetcher.fetch_news()
        today_counts = analyzer.analyze_text(text)
        yesterday_counts = storage.load_yesterday_counts()

        print("\n📊 Сегодняшние упоминания тем:")
        for word, count in today_counts.items():
            r_word = config.KEYWORDS_MAPPING.get(word, word)
            print(f"{r_word}: {count}")
            log.info(f"{r_word}: {count}")

        compare_and_alert(today_counts, yesterday_counts)
        storage.save_today_counts(today_counts)

        print("\n✅ Завершено.")
        log.info("✅ Завершено.")
    except Exception as e:
        log.error(f"❌ Ошибка: {e}")
        sys.exit(1)
    
    finally:
        # Логируем использование ресурсов
        end_time = time.time()
        total_time = end_time - start_time

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"\n✅ Завершено за {total_time:.2f} секунд, пик памяти: {peak / 1024:.2f} KB.")
        log.info(f"✅ Завершено за {total_time:.2f} секунд, пик памяти: {peak / 1024:.2f} KB.")

if __name__ == "__main__":
    main()
