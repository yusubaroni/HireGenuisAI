import streamlit as st
import requests

st.title("HireGenius AI – Smart Interview Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("💬 Your answer or question:")

if st.button("Send"):
    if user_input:
        response = requests.get("http://127.0.0.1:8000/interview")
        st.session_state.messages.append({"user": user_input, "ai": response.json()["message"]})

for chat in st.session_state.messages:
    st.write(f"**You:** {chat['user']}")
    st.write(f"**AI:** {chat['ai']}")
