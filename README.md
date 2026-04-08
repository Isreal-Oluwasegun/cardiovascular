# Cardiovascular Disease Risk Prediction App

This project provides a Streamlit interface for predicting cardiovascular disease risk using a trained machine learning model (`.pkl`). The interface allows manual input of patient variables without requiring dataset uploads. The application is containerized with Docker for easy deployment.

## Features
- Manual input of patient variables:
  - Age
  - Gender
  - Systolic and Diastolic Blood Pressure
  - Cholesterol level
  - Glucose level
  - Smoking status
  - Alcohol intake
  - BMI
- Model prediction using a pre-trained `.pkl` file
- Probability output with risk classification
- Session history to track multiple patient inputs
- Option to export predictions as CSV or PDF
- Feature importance visualization for interpretability

## Requirements
- Python 3.10+
- Streamlit
- NumPy
- scikit-learn
- Plotly (for charts)

Install dependencies:
```bash
pip install -r requirements.txt
