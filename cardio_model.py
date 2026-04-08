import streamlit as st
import pickle
import numpy as np

# Load your trained model
with open("cardio_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="CVD Risk Predictor", layout="wide")

st.title("Cardiovascular Disease Risk Prediction")
st.markdown("Enter patient details below to estimate CVD risk.")

# Sidebar for inputs
st.sidebar.header("Patient Information")

age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=40)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
systolic_bp = st.sidebar.number_input("Systolic BP", min_value=80, max_value=250, value=120)
diastolic_bp = st.sidebar.number_input("Diastolic BP", min_value=50, max_value=150, value=80)
cholesterol = st.sidebar.selectbox("Cholesterol Level", [1, 2, 3])  # categorical coding
glucose = st.sidebar.selectbox("Glucose Level", [1, 2, 3])          # categorical coding
smoke = st.sidebar.selectbox("Smoker", ["No", "Yes"])
alcohol = st.sidebar.selectbox("Alcohol Intake", ["No", "Yes"])
bmi = st.sidebar.number_input("bmi", min_value=10.0, max_value=60.0, value=25.0)

# Convert inputs to numeric features
gender_val = 1 if gender == "Male" else 0
smoke_val = 1 if smoke == "Yes" else 0
alcohol_val = 1 if alcohol == "Yes" else 0

features = np.array([[age, gender_val, systolic_bp, diastolic_bp,
                      cholesterol, glucose, smoke_val, alcohol_val, bmi]])

# Prediction
if st.sidebar.button("Predict"):
    prob = model.predict_proba(features)[0][1]
    st.metric(label="Predicted CVD Risk Probability", value=f"{prob:.2%}")
    if prob > 0.5:
        st.error("High risk of CVD detected!")
    else:
        st.success("Low risk of CVD")
