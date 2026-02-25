from fastapi import FastAPI
from .ai_logic import analyze_resume
from .matching import calculate_match

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "AI System Active"}

@app.post("/process-matching")
def process(resume_text: str, job_text: str):
    # 1. Анализируем резюме через файл ai_logic.py
    student_data = analyze_resume(resume_text)
    
    # 2. Сравниваем с вакансией через matching.py
    result = calculate_match(student_data, job_text)
    
    return result
