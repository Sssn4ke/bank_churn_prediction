# Bank Customer Churn Prediction

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.49.1-orange)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.4.2-green)
![Docker](https://img.shields.io/badge/Docker-✅-lightblue)

## Metrics
![Accuracy](https://img.shields.io/badge/Accuracy-0.96-brightgreen)
![F1--Score](https://img.shields.io/badge/F1--Score-0.90-green)

ML модель для прогнозирования оттока клиентов банка с веб-интерфейсом.

## О проекте

Проект решает задачу прогнозирования оттока клиентов банка. Модель машинного обучения анализирует  характеристики клиентов и предсказывает вероятность их ухода с точностью **96%**.

## Ключевые особенности

-   **Точность**: F1-Score = 0.90 для миноритарного класса
-   **Интерактивный интерфейс**: Streamlit-приложение с визуализацией
-   **Простота развертывания**: Docker-контейнеризация
-   **Интерпретируемость**: Анализ важности признаков модели

## Результаты

| Метрика | Значение |
|---------|----------|
| **Accuracy** | 0.96 |
| **F1-Score** | 0.90 |
| **Recall** | 0.89 |
| **Precision** | 0.91 |

## Технологический стек

-   **Язык программирования**: Python 3.11
-   **ML фреймворк**: Scikit-learn, Gradient Boosting
-   **Веб-интерфейс**: Streamlit
-   **Контейнеризация**: Docker
-   **Анализ данных**: Pandas, NumPy, Matplotlib

## Скриншоты

### Главный интерфейс
![Главный интерфейс приложения](images/Predict_bank_churn.png)

### Пример предсказания
![Предсказание модели](images/model_result.png)

### Главные признаки
![Признаки влияющие больше всего на предсказание](images/Feature_importances.png)

## Запуск

```bash
# Клонировать репозиторий
git clone https://github.com/your-username/bank-churn-prediction.git

# Установить зависимости
pip install -r requirements.txt

# Запустить приложение
streamlit run streamlit_app.py

### Docker-запуск
```bash
# Собрать образ
docker build -t churn-app .

# Запустить контейнер
docker run -p 8501:8501 churn-app
