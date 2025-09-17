# Базовый образ с Python 3.11 на легковесной OS Linux
FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл с зависимостями
COPY requirements.txt .

# Устанавливаем все зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем ВЕСЬ проект в контейнер (кроме того, что в .dockerignore)
COPY . .

# Открываем порт, на котором работает Streamlit
EXPOSE 8501

# Команда запуска приложения при старте контейнера
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]