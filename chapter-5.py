import streamlit as st
import requests

st.title("Live Currncy Converter")
amount = float(st.number_input("Enter The amout in INR", min_value = 1))

targeted_currency = st.selectbox("Convert To: ",["USD","EUR","GBP","JPY"])

if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][targeted_currency]
        converted_value = rate*amount
        st.success(f"{amount} INR = {converted_value:.5f} {targeted_currency}")
    else:
        st.error("Failed To Fetch Conversion Rate")