import os
import json
from openai import OpenAI

# Инициализация клиента. Ключ подтянется из переменных окружения
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_resume(text):
    """Функция для извлечения навыков из резюме студента через ИИ"""
    prompt = f"""
    Проанализируй текст резюме и выдели навыки в формате JSON:
    {{
      "hard_skills": ["навык1", "навык2"],
      "soft_skills": ["навык1", "навык2"],
      "projects": ["проект1"]
    }}
    Текст: {text}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        response_format={ "type": "json_object" }
    )
    return json.loads(response.choices[0].message.content)
