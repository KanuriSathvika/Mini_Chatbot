


# # app/chatbot.py
# import streamlit as st
# import google.generativeai as genai
# from google.generativeai import GenerativeModel
# # import streamlit as st

# def initialize_chat(model_name, session_name):
#     genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

#     # If session doesn't exist, create it
#     if session_name not in st.session_state.sessions:
#         st.session_state.sessions[session_name] = []

#     # ✅ If model was changed mid-convo — reload the chat object with existing history
#     current_model = st.session_state.get("chat_model")
#     if current_model != model_name or "chat" not in st.session_state:
#         model = genai.GenerativeModel(model_name)
#         st.session_state.chat = model.start_chat(
#             history=st.session_state.sessions[session_name]
#         )
#         st.session_state.chat_model = model_name



# def initialize_empty_chat():
#     model = st.session_state.chat_model  # or default model if needed
#     gen_model = GenerativeModel(model)
#     return gen_model.start_chat(history=[])




import google.generativeai as genai
import streamlit as st

def initialize_chat():
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    st.session_state.chat = genai.GenerativeModel(st.session_state.chat_model).start_chat()
