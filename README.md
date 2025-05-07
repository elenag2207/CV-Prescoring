# 📊 CV Scoring App

Веб-приложение на Python + Streamlit, которое анализирует резюме кандидата на соответствие вакансии с помощью GPT-4o.

---

## 🚀 Функциональность

- 📌 Ввод описания вакансии и резюме (или ссылки на hh.ru)
- 🧠 GPT-модель анализирует соответствие
- 💬 Краткий вывод с пояснением и финальной оценкой от 1 до 10
- 🔗 Возможность парсинга по ссылке с hh.ru (вакансия и резюме)

---

## 🧰 Используемые технологии

- `Python 3.10+`
- `Streamlit`
- `OpenAI API (GPT-4o-mini)`
- `BeautifulSoup` для парсинга HTML с hh.ru

---

## 🛠 Установка

```bash
git clone https://github.com/elenag2207/cv-scoring-app.git
cd cv-scoring-app
python3 -m venv venv
source venv/bin/activate  # для macOS/Linux
pip install -r requirements.txt
