import requests
import logging
from config import DEEPSEEK_API_KEY

logger = logging.getLogger(__name__)

def deepseek_generate(prompt):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 500
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка при запросе к API: {e}")
        return f"Ошибка при запросе к API: {e}"
    except KeyError:
        logger.error("Ошибка при обработке ответа от API.")
        return "Ошибка при обработке ответа от API."