# NewsWatcher

**NewsWatcher** — это система для автоматического анализа новостей, отслеживания ключевых тем и отправки уведомлений в Telegram при повышенном интересе к определённым темам.

## Стек

- Python 3.8+
- feedparser
- python-telegram-bot
- python-dotenv
- GitHub Actions CI/CD

## 📦 Установка и настройка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/ТВОЙ_ЮЗЕР/news-watcher.git
   cd news-watcher
   ```

2. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

3. Получите **Telegram Bot API token** и **Chat ID**.
4. Настройте переменные в `news_watcher.py`:
   - `BOT_TOKEN` — токен бота.
   - `CHAT_ID` — ID чата для получения уведомлений.

## Локально
   1. Установить нужный Python
   ```bash
   pyenv install 3.8.6
   pyenv local 3.8.6
   ```

   2. Создать виртуальное окружение
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   3. Установить зависимости
   ```
   pip install -r requirements.txt
   ```

   4. Заполнить .env
   ```
   nano .env
   ```

   5. Запустить
   ```
   python news_watcher.py
   ```


## 🛠️ Структура проекта

```
news-watcher/
├── app/                  # Весь код приложения
│   ├── __init__.py
│   ├── parser.py          # Парсер новостей
│   ├── analyzer.py        # Аналитика общего фона
│   └── config.py          # Конфигурации
├── venv/                  # (Локальное виртуальное окружение, в .gitignore)
├── logs/                  # Логи работы (ротация логов можно будет добавить)
│   └── app.log
├── requirements.txt       # Зависимости проекта
├── news_watcher.py        # Главный файл запуска
├── .gitignore             # Игнорируем лишние файлы
└── README.md              # Описание проекта
```

- **news_watcher.py** — основной скрипт для анализа новостей и отправки уведомлений.
- **requirements.txt** — список зависимостей (например, `feedparser`, `python-telegram-bot`).
- **.github/workflows/deploy.yml** — конфигурация CI/CD через GitHub Actions.

## 🚀 Автоматизация через GitHub Actions

1. Настройте CI/CD с использованием **GitHub Actions** для автоматического запуска скрипта при пуше изменений в репозиторий.
2. Пример конфигурации в `.github/workflows/deploy.yml`.

## ⚙️ Логгирование и валидация

- Валидация ошибок добавлена для защиты от сбоев в процессе получения новостей или отправки сообщений.
- Логгирование записывает ключевые действия и ошибки в процессе работы скрипта.

## 📦 версионирование проекта

| Этап                       | Что делать                           |
|:----------------------------|:-------------------------------------|
| Указать версию в коде        | `__version__ = "0.1.0"`              |
| Делать git-теги              | `git tag v0.1.0 && git push --tags` |



---

📅 **Дата обновления**: April 2025
