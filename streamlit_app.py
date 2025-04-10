import streamlit as st
import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="🏡 Home Value Estimator", layout="centered")

st.title("🏠 What's Your Home Worth?")
st.write("Fill out the form below and our AI will estimate your home's value.")

name = st.text_input("Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
address = st.text_input("Street Address")
zip_code = st.text_input("ZIP Code")
bedrooms = st.number_input("Bedrooms", min_value=0)
bathrooms = st.number_input("Bathrooms", min_value=0)
condition = st.selectbox("Condition", ["Excellent", "Good", "Fair", "Needs Work"])
renovations = st.text_area("Recent Renovations (optional)")

if st.button("Estimate Home Value"):
    prompt = f"Estimate the home value for this property:\nAddress: {address}, ZIP: {zip_code}\nBedrooms: {bedrooms}, Bathrooms: {bathrooms}\nCondition: {condition}\nRenovations: {renovations}\n"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a real estate assistant trained in home price estimation."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )

    estimate = response['choices'][0]['message']['content']
    st.success(f"🏡 Based on your info, here’s the estimate:\n\n{estimate}")
    st.info("You'll get a copy of this in your email too!")
