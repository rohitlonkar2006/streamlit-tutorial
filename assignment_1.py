import streamlit as st
from datetime import date

st.title("Welcome Rohit,You Can Easily Count Your Age!")
st.text("Just Select The DOB.")


def count(dob):
    today = date.today()
    age = today.year - dob.year
    return age


dob = st.date_input("Select You Date Of Birth")
st.success(f"Your Age Is {count(dob)}")
