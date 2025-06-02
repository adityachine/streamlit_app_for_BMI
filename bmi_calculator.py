import streamlit as st 
import pandas as pd 

st.title("BMI Calculator")
st.write("this is a simple BMI calculator that takes your height and weight and calculates your BMI for your health status")

height = st.slider("Enter your height (in cm):",100,250,170)
weight = st.slider("Enter your weight (in kg):",40,200,70)

bmi = weight / ((height/100) **2)

st.write(f"Your BMI is: {bmi:.2f}")

st.write(f"Your BMI Categories ###")
st.write(f"- Underweight your BMI is less than 18.5")
st.write(f"- Normal weight your BMI is between 18.5 and 24.9")
st.write(f"- overweight your BMI is Between 25 and 29.9")
st.write(f"- Obesity your BMI is 30 or more")


if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

st.success(f"🩺 You are **{category}** based on your BMI.")

from openai import OpenAI 
client = OpenAI(api_key="sk-...")

def get_tips_openai(bmi, height, weight):
    prompt = f"My BMI is {bmi:.2f}, height: {height} cm, weight: {weight} kg. Suggest 3 tips to improve my health."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a fitness assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content