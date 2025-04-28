import json
import os
from app import config

def load_yesterday_counts():
    if os.path.exists(config.YESTERDAY_FILE):
        with open(config.YESTERDAY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_today_counts(counts):
    with open(config.YESTERDAY_FILE, "w") as f:
        json.dump(counts, f)
