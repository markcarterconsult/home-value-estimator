import streamlit as st

st.set_page_config(page_title="Home Value Checker", layout="centered")

st.title("🏠 Home Value Estimator")
st.write("Let's see if this baby runs!")

if st.button("Estimate"):
    st.success("🎉 It works! Now let's add your full form and AI logic.")
