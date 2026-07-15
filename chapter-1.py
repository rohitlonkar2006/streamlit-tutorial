import streamlit as st

st.title("Hello From Rohit's App")
st.subheader("Build with streamlit")
st.text("Welcome to yuor first interactive app")
st.write("Choose you fav type of agent ex., (HealthAgent, SmmaryWriter)")

Agent = st.selectbox("Your Fav Agent:",["HealthAgent", "SummaryWriter", "ResearchAgent"])
st.write(f"You Choose {Agent} Agent.Excellent Choise...!")

st.success("Your Chai Has Brewed...!")