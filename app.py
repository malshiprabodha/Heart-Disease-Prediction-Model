import streamlit as st
import pandas as pd
import joblib

model = joblib.load("heart_disease_model.pkl")

st.set_page_config(
page_title="Heart Disease Prediction",
page_icon="❤️",
layout="centered"
)

st.title("❤️ Heart Disease Prediction System")
st.write("Enter patient information to predict the likelihood of heart disease.")

age = st.number_input("Age", min_value=1, max_value=120, value=50)

sex = st.selectbox(
"Sex",
["Male", "Female"]
)

chest_pain = st.selectbox(
"Chest Pain Type",
[
"Typical Angina",
"Atypical Angina",
"Non-Anginal Pain",
"Asymptomatic"
]
)

resting_bp = st.number_input(
"Resting Blood Pressure (mmHg)",
min_value=50,
max_value=250,
value=120
)

cholesterol = st.number_input(
"Cholesterol (mg/dL)",
min_value=50,
max_value=700,
value=200
)

fasting_bs = st.selectbox(
"Fasting Blood Sugar > 120 mg/dL?",
["No", "Yes"]
)

resting_ecg = st.selectbox(
"Resting ECG Result",
[
"Normal",
"ST-T Wave Abnormality",
"Left Ventricular Hypertrophy"
]
)

max_hr = st.number_input(
"Maximum Heart Rate",
min_value=60,
max_value=220,
value=150
)

exercise_angina = st.selectbox(
"Exercise-Induced Angina",
["No", "Yes"]
)

oldpeak = st.number_input(
"Oldpeak (ST Depression)",
min_value=0.0,
max_value=10.0,
value=1.0,
step=0.1
)

st_slope = st.selectbox(
"ST Slope",
[
"Upward",
"Flat",
"Downward"
]
)

if st.button("Predict"):
    sex = 1 if sex == "Male" else 0

    chest_pain_map = {
        "Typical Angina": 1,
        "Atypical Angina": 2,
        "Non-Anginal Pain": 3,
        "Asymptomatic": 4
    }

    fasting_bs = 1 if fasting_bs == "Yes" else 0

    ecg_map = {
        "Normal": 0,
        "ST-T Wave Abnormality": 1,
        "Left Ventricular Hypertrophy": 2
    }

    exercise_angina = 1 if exercise_angina == "Yes" else 0

    st_slope_map = {
        "Upward": 1,
        "Flat": 2,
        "Downward": 3
    }

    sample = pd.DataFrame([{
        'age': age,
        'sex': sex,
        'chest pain type': chest_pain_map[chest_pain],
        'resting bp s': resting_bp,
        'cholesterol': cholesterol,
        'fasting blood sugar': fasting_bs,
        'resting ecg': ecg_map[resting_ecg],
        'max heart rate': max_hr,
        'exercise angina': exercise_angina,
        'oldpeak': oldpeak,
        'ST slope': st_slope_map[st_slope]
    }])

    prediction = model.predict(sample)[0]
    probability = model.predict_proba(sample)[0][1]

    if prediction == 1:
        st.error("⚠️ Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease Detected")

    st.metric(
        "Probability of Heart Disease",
        f"{probability * 100:.2f}%"
    )