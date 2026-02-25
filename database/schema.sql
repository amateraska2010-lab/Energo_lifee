CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    university VARCHAR(255),
    skills JSONB,
    experience TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE vacancies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    company VARCHAR(255),
    required_skills JSONB,
    description TEXT
);

CREATE TABLE matches (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(id),
    vacancy_id INTEGER REFERENCES vacancies(id),
    match_score FLOAT,
    recommendations TEXT
);
