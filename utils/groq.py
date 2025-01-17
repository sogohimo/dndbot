import requests
import logging
from config import GROQ_API_KEY

logger = logging.getLogger(__name__)

def groq_generate(prompt):
    url = "https://api.groq.com/v1/chat/completions"  # URL API Groq
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3.3-70b-versatile",  # Используемая модель
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 500  # Максимальное количество токенов в ответе
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Проверяем, есть ли ошибки в ответе
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка при запросе к Groq API: {e}")
        return f"Ошибка при запросе к Groq API: {e}"
    except KeyError:
        logger.error("Ошибка при обработке ответа от API.")
        return "Ошибка при обработке ответа от API."