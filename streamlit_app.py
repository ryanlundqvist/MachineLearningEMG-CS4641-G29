import streamlit as st

st.title("🤖 Machine Learning | EMG | G29")
st.header("Proposal Report", divider="rainbow")
st.subheader("Introduction & Background", divider="blue")
st.write("What is EMG:")
st.write()
st.subheader("Problem Definition", divider="blue")
st.subheader("Methods", divider="blue")
st.subheader("Expected Results & Discussion", divider="blue")
st.subheader("References", divider="blue")

st.write(
    "What is EMG:
 Bioelectrical signals generated by muscle cells when they are activated. 
Captured using electrodes placed on a skin surface. 
In regards to our dataset, The Myo Thalmic bracelet captures signals from the forearm. It does this by utilizing 8 EMG sensors and a bluetooth module. 
What is EMG Gesture Classification? 
Process in which electric signals gendered by muscle contractions are monitored inorder to identify specific gestures. 
"
)

st.subheader("Gantt Chart", divider="blue")
st.image("4641_gantt.png")
st.subheader("Contributions")
st.image("4641_proposal_contributions.png")


