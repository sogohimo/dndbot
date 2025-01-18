from groq import Groq
import logging
from config import GROQ_API_KEY

logger = logging.getLogger(__name__)

def groq_generate(prompt):
    client = Groq(api_key=GROQ_API_KEY)
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Убедитесь, что модель актуальна
            messages=[{"role": "user", "content": prompt}],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=False,  # Отключаем потоковую передачу для упрощения
            stop=None,
        )
        return completion.choices[0].message.content
    except Exception as e:
        logger.error(f"Ошибка при запросе к Groq API: {e}")
        return f"Ошибка при запросе к Groq API: {e}"