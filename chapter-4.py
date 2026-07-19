import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

st.title("Agent Sales Dashboard")

file = st.file_uploader("Upload Your CSV Fie", type = ["CSV"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)
    
if file:
    st.subheader("Summary Stats")
    st.write(df.describe())
    
if file:
    cities = df["city"].unique()
    selected_city = st.selectbox("Filter By City", cities)
    filtered_data = df[df["city"] == selected_city]
    st.dataframe(filtered_data)
    
st.line_chart(df["revenue"])
    