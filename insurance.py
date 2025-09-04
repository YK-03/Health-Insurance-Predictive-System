import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load the dataset
insurance_dataset = pd.read_csv('insurance.csv')

insurance_dataset.replace({'sex': {'male': 0, 'female': 1}}, inplace=True)
insurance_dataset.replace({'smoker': {'yes': 1, 'no': 0}}, inplace=True)
insurance_dataset.replace({'region': {'southeast': 0, 'southwest': 1, 'northeast': 2, 'northwest': 3}}, inplace=True)

X = insurance_dataset.drop(columns='charges', axis=1)
Y = insurance_dataset['charges']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

regressor = LinearRegression()
regressor.fit(X_train, Y_train)

def preprocess_input_data(age, sex, bmi, children, smoker, region):
    input_data = (age, sex, bmi, children, smoker, region)
    return np.asarray(input_data).reshape(1, -1)

def predict_insurance_cost(model, input_data):
    prediction = model.predict(input_data)
    return prediction[0]

def calculate_bmi(h, w):
    if h > 0:
        return w / ((h / 100) ** 2)
    return 0

st.title('Insurance Cost Prediction')

age = st.slider('Age', min_value=18, max_value=100, value=30)
sex = st.radio('Gender', ['Male', 'Female'])
height = st.number_input('Height (in cm)', min_value=50.0, max_value=250.0, value=170.0)
weight = st.number_input('Weight (in kg)', min_value=10.0, max_value=200.0, value=70.0)
children = st.number_input('Number of Children', min_value=0, max_value=10, value=1)
smoker = st.radio('Smoker', ['Yes', 'No'])
region = st.selectbox('Region', ['Southeast', 'Southwest', 'Northeast', 'Northwest'])

sex_mapping = {'Male': 0, 'Female': 1}
smoker_mapping = {'Yes': 1, 'No': 0}
region_mapping = {'Southeast': 0, 'Southwest': 1, 'Northeast': 2, 'Northwest': 3}

sex_encoded = sex_mapping.get(sex)
smoker_encoded = smoker_mapping.get(smoker)
region_encoded = region_mapping.get(region)
calculated_bmi = calculate_bmi(height, weight)

if calculated_bmi > 0:
    input_data = preprocess_input_data(age, sex_encoded, calculated_bmi, children, smoker_encoded, region_encoded)
    if st.button('Predict Insurance Cost'):
        prediction = predict_insurance_cost(regressor, input_data)
        st.success(f'The predicted insurance cost is: {prediction:.2f} USD')
else:
    st.error("Please enter valid height and weight values.")
