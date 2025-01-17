import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Токен Telegram-бота
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # API-ключ Groq