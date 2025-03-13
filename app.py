import numpy as np
import streamlit as st
import joblib

logo_url = "logo.png"
banner_path = "banner.jpg"
st.image(logo_url, width=100)
st.write("# Insurance App")
st.image(banner_path)

age = st.number_input("Enter your age", step = 1)
height_ft = st.number_input("Enter your height in feet", step = 1, value = 5)
height_inch = st.number_input("Enter inch part of your height", step = 1, value = 5)
weight_kg = st.number_input("Enter your weight in kg")
height_meter = height_ft*0.3048 + height_inch*0.0254
bmi = round(weight_kg/height_meter**2,2)
smoker = st.selectbox("Enter your smoking status?",("Yes","No"))
children = st.selectbox("Enter number of children",(0,1,2,3,4))

test_data = np.array([[age, bmi, smoker, children]])
st.write(test_data)

#Load Model
model  = joblib.load("insurance_joblib")

# Predict Button
if st.button("Predict"):
    y_pred = model.predict(test_data)
    amount = np.round(y_pred**2,2)[0]
    st.write(f"## Your Insurance Premium amount is: ${amount}")