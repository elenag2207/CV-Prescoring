import streamlit as st
import os
from openai import OpenAI
from parse_app import get_html, extract_vacancy_data, extract_resume_data

# 🔐 Подставь сюда свой API-ключ
client = openai.Client(
    api_key=os.getenv("OPENAI_API_KEY")
)

# 📌 Системный промпт
SYSTEM_PROMPT = """
Проскорь кандидата, насколько он подходит для данной вакансии.

Сначала напиши короткий анализ, который будет пояснять оценку.
Отдельно оцени качество заполнения резюме (понятно ли, с какими задачами сталкивался кандидат и каким образом их решал?).
Эта оценка должна учитываться при выставлении финальной оценки — нам важно нанимать таких кандидатов, которые могут рассказать про свою работу.
Потом представь результат в виде оценки от 1 до 10.
""".strip()

def request_gpt(system_prompt, user_prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        max_tokens=1000,
        temperature=0,
    )
    return response.choices[0].message.content

# Интерфейс
st.title("CV Scoring App")

job_url = st.text_input("🔗 Вставьте ссылку на вакансию")
resume_url = st.text_input("🔗 Вставьте ссылку на резюме")

if st.button("🔍 Проанализировать соответствие"):
    with st.spinner("Парсим и отправляем в GPT..."):
        try:
            job_html = get_html(job_url).text
            resume_html = get_html(resume_url).text

            job_text = extract_vacancy_data(job_html)
            resume_text = extract_resume_data(resume_html)

            # Вывод данных
            st.subheader("📌 Описание вакансии")
            st.markdown(job_text)

            st.subheader("📋 Резюме кандидата")
            st.markdown(resume_text)

            # GPT
            full_prompt = f"# ВАКАНСИЯ\n{job_text}\n\n# РЕЗЮМЕ\n{resume_text}"
            response = request_gpt(SYSTEM_PROMPT, full_prompt)

            st.subheader("📊 Результат анализа")
            st.markdown(response)

        except Exception as e:
            st.error(f"❌ Произошла ошибка: {e}")
