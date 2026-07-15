import streamlit as st

st.title("Agent Maker App")

if st.button("Make Chai"):
    st.success("Your Agent Is Being Brewed...!")

st.write("Select Agents:")
agent1 = st.checkbox("HealthAgent")
agent2 = st.checkbox("SummaryWriterAgent")
agent3 = st.checkbox("ResearchAgent")

if agent1:
    st.write("HealthAgent Selected..!")
    
if agent2:
        st.write("SummaryWriterAgent Selected..!")

if agent3:
        st.write("ResearchAgent Selected..!")
        
        
agent_type = st.radio("Pick Your Agent Behaviour:",["Funny","Angry","Strict"])
st.write(f"Selected Base {agent_type}")

output_type = st.selectbox("Choose output type",["Structured Output","Long Output","Summary"])

accuracy = st.slider(
    "Agent Temperature",
    min_value=0.0,
    max_value=2.0,
    value=0.2,
    step=0.1
)
