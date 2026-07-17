import streamlit as st

st.title("Agent Poll")

col1,col2 = st.columns(2)

with col1:
    st.header("Memory Agent")
    vote1 = st.button("Vote Memory Agent")
    st.image("https://imgs.search.brave.com/Ox7GpmnSmkrIW5qtE_9UQkwLXi8hglH89njpCtTb630/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93d3cu/bGVvbmllbW9uaWdh/dHRpLmNvbS9ibG9n/L2ltYWdlcy9hZ2Vu/dC1tZW1vcnkud2Vi/cA", width = 200)

with col2:
    st.header("summary Agent")
    vote2 = st.button("Vote summary Agent")  
    st.image("https://imgs.search.brave.com/pfE5M2AtM1e03SDwzaAhesvHJd2LoP8SkIRItWlUe4s/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLnl0/aW1nLmNvbS92aV93/ZWJwL1l4TVY2THRG/czFzL2hxZGVmYXVs/dC53ZWJw", width = 200) 

if vote1:
    st.success("Thanks For Voting Memory Agent..!")

elif vote2:
    st.success("Thanks for Voting summary Agent..!")
    
home = st.sidebar.button("Home")
start = st.sidebar.button("Start")
pf = st.sidebar.button("Profile")
about = st.sidebar.button("About Us")

if(home):
    st.success("Its Home Section")
    
if(start):
    st.success("Its Start Section")
    
if(pf):
    st.success("Its Profile Section")
    
if(about):
    st.success("Its Home Section")
    
with st.expander("Click On Expand Icon"):
    st.write("""
             1. Click On Start
             2. Select Your Favourite Agent
             3. Start Your Journey
             """)