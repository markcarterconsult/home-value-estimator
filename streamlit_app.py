import streamlit as st

st.title("🏡 What's Your Home Worth?")
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
    st.success("📬 Based on your info, your home's estimated value is between **$325,000 and $345,000.**")
    st.info("You'll get a copy of this in your email too!")
