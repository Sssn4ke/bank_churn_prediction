import streamlit as st
import joblib
import pandas as pd
import numpy
import matplotlib.pyplot as plt
import sklearn
from sklearn.ensemble import GradientBoostingClassifier

# Создаем вкладки
tab1, tab2 = st.tabs(["Predicting Bank Customer Churn", "Feature importance"])

# Содержимое первой вкладки
with tab1:
    st.title('Predicting Bank Customer Churn')
    st.write('This app predicts whether a customer will leave a bank based on an ML model.')

    model = joblib.load('best_model.joblib')

    gender_modified = {'M': 0, 'F': 1}
    Card_Category_modified = {'Blue': 0, 'Silver': 1, 'Gold': 2, 'Platinum': 3}
    Education_Level_modified = {'High School': 0, 'Graduate': 1, 'Uneducated': 2, 'Unknown': 3, 'College': 4,
                                'Post-Graduate': 5, 'Doctorate': 6}
    Marital_Status_modified = {'Married': 0, 'Single': 1, 'Unknown': 2, 'Divorced': 3}
    Income_Category_modified = {'$60K - $80K': 0, 'Less than $40K': 1, '$80K - $120K': 2, '$40K - $60K': 3,
                                '$120K +': 4, 'Unknown': 5}

    st.sidebar.header('Client parameters:')
    Customer_Age = st.sidebar.slider('Age', 18, 100, 45)
    Dependent_count = st.sidebar.slider('Dependent count', 0, 10, 2)
    Gender = st.radio("Select sex", options=list(gender_modified.keys()))
    Education_level = st.selectbox("Select education", options=list(Education_Level_modified.keys()))
    Marital_status = st.selectbox("Select marital status", options=list(Marital_Status_modified.keys()))
    Income_category = st.selectbox("Select income category", options=list(Income_Category_modified.keys()))
    Card_category = st.selectbox("Select card", options=list(Card_Category_modified.keys()))
    Months_on_book = st.sidebar.number_input('Period of relationship with bank', 0, 56, 2)
    Total_Relationship_Count = st.sidebar.number_input('Total no. of products held by the customer', 1, 8, 2)
    Months_Inactive_12_mon = st.sidebar.number_input('No. of months inactive in the last 12 months', 0, 12, 2)
    Contacts_Count_12_mon = st.sidebar.number_input('No. of Contacts in the last 12 months', 0, 12, 2)
    Credit_Limit = st.sidebar.number_input('Credit Limit', 1440, 35000, 2000)
    Total_Revolving_Bal = st.sidebar.number_input('Total Revolving Balance', 0, 2600, 50)
    Total_Amt_Chng_Q4_Q1 = st.sidebar.number_input('Change in Transaction Amount (Q4 over Q1)', 0, 4, 2)  # ?????????
    Total_Trans_Amt = st.sidebar.number_input('Total Transaction Amount (Last 12 months)', 510, 19000, 1000)
    Total_Trans_Ct = st.sidebar.number_input('Total Transaction Count (Last 12 months)', 10, 139, 12)
    Total_Ct_Chng_Q4_Q1 = st.sidebar.number_input('Change in Transaction Count (Q4 over Q1)', 0, 4, 2)
    Avg_Utilization_Ratio = st.sidebar.number_input('Average Card Utilization Ratio', 0.0, 1.0, 0.5)

    gender_encoded = gender_modified[Gender]
    card_encoded = Card_Category_modified[Card_category]
    education_encoded = Education_Level_modified[Education_level]
    marital_encoded = Marital_Status_modified[Marital_status]
    income_encoded = Income_Category_modified[Income_category]

    if st.sidebar.button('Predict'):
        # Собираем все данные в DataFrame
        input_data = pd.DataFrame([[Customer_Age, Dependent_count, Months_on_book, Total_Relationship_Count,
                                    Months_Inactive_12_mon, Contacts_Count_12_mon, Credit_Limit, Total_Revolving_Bal,
                                    Total_Amt_Chng_Q4_Q1, Total_Trans_Amt, Total_Trans_Ct, Total_Ct_Chng_Q4_Q1,
                                    Avg_Utilization_Ratio, gender_encoded, card_encoded, education_encoded,
                                    marital_encoded, income_encoded]],
                                  columns=['Customer_Age', 'Dependent_count', 'Months_on_book',
                                           'Total_Relationship_Count', 'Months_Inactive_12_mon',
                                           'Contacts_Count_12_mon', 'Credit_Limit',
                                           'Total_Revolving_Bal', 'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt',
                                           'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1', 'Avg_Utilization_Ratio',
                                           'gender_encoded',
                                           'card_encoded', 'education_encoded', 'marital_encoded', 'income_encoded'])

        prediction = model.predict(input_data)[0]
        prediction_proba = model.predict_proba(input_data)[0]

        if prediction == 0:
            st.error(f'Probability of Attrited Customer: {prediction_proba[0] * 100:.2f}%')
        else:
            st.success(f'Probability of Existing Customer: {prediction_proba[1] * 100:.2f}%')

        fig, ax = plt.subplots()
        ax.bar(['Attrited', 'Existing'], prediction_proba, color=['red', 'green'])
        ax.set_ylabel('Probability')
        st.pyplot(fig)


# Содержимое второй вкладки (пример)
with tab2:
    st.title('Feature importance')
    # Создаем данные для таблицы
    data = {
        'Feature': ['Total_Trans_Ct', 'Total_Trans_Amt', 'Total_Revolving_Bal', 'Total_Ct_Chng_Q4_Q1', 'Total_Amt_Chng_Q4_Q1', 'Total_Relationship_Count', 'Customer_Age', 'Credit_Limit',
                    'Months_Inactive_12_mon'],
        'Importance': [0.481941, 0.182238, 0.100945, 0.066278, 0.049074, 0.047537, 0.019342, 0.017722, 0.011684]
    }

    # Создаем DataFrame
    df = pd.DataFrame(data)


    st.table(df)

