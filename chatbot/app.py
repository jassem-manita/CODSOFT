import streamlit as st
from src import chatbot

def main():
    st.title("Streamlit Role-Based Chatbot")

    user_input = st.text_input("You:")
    if user_input:
        intent = chatbot.recognize_intent(user_input)
        response = chatbot.generate_response(intent)
        st.text_area("Chatbot:", response)

if __name__ == "__main__":
    main()
