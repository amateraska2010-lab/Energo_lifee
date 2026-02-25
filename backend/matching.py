import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def calculate_match(student_skills, vacancy_requirements):
    """Сравнивает навыки студента и требования вакансии через AI"""
    prompt = f"""
    Сравни навыки студента и требования вакансии.
    Студент: {student_skills}
    Вакансия: {vacancy_requirements}

    Верни JSON с процентом соответствия (0-100), списком недостающих навыков и советом.
    """
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        response_format={ "type": "json_object" }
    )
    return json.loads(response.choices[0].message.content)
