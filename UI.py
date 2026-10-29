import streamlit as st
import joblib
import numpy as np

#load model
model=joblib.load("model_joblib")

#page configuration
st.set_page_config(page_title="Salary Predictor",layout="centered")

#title
st.title("Salary Prediction App")
st.write("Enter your years of experience to predict salary")

#input
experience=st.number_input(
"Years of Experience",min_value=0.0,max_value=50.0,value=1.0,step=0.5)

#prediction
if st.button("Predict Salary"):
    try:
        #model expects 2D array
        input_data=np.array([[experience]])
        prediction=model.predict(input_data)
        st.success(f"Predicted Salary:₹{prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"Error:{e}")
