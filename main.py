

# # # main.py

# # import streamlit as st
# # from app.ui import display_chat_ui
# # from app.chatbot import initialize_chat

# # # ✅ FIRST Streamlit command — must be before sidebar, title, etc.
# # st.set_page_config(page_title="💬 Gemini Chatbot", layout="centered")

# # # Sidebar for model selection
# # model_name = st.sidebar.selectbox(
# #     "Select Gemini Model",
# #     options=["gemini-1.5-flash", "gemini-1.5-flash-8b","gemini-2.0-flash","gemini-2.0-flash-thinking-exp-01-21","gemini-2.5-pro-preview-03-25"],
# #     index=0
# # )

# # # Initialize chat with selected model
# # initialize_chat(model_name)

# # # Display UI
# # display_chat_ui()



# #     # options=["gemini-1.5-flash", "gemini-1.5-flash-8b","gemini-2.0-flash","gemini-2.0-flash-thinking-exp-01-21","gemini-2.5-pro-preview-03-25"],




# # # main.py
# # import streamlit as st
# # from app.ui import display_chat_ui
# # from app.chatbot import initialize_chat

# # st.set_page_config(page_title="💬 Gemini Chatbot", layout="centered")

# # # List of models
# # model_name = st.sidebar.selectbox(
# #     "Select Gemini Model",
# #     options=["gemini-1.5-flash", "gemini-1.5-flash-8b","gemini-2.0-flash","gemini-2.0-flash-thinking-exp-01-21"],
# #     index=0
# # )

# # # Initialize sessions dictionary if not present
# # if "sessions" not in st.session_state:
# #     st.session_state.sessions = {}  # dict: session_name → history list
# #     st.session_state.active_session = ""

# # # Sidebar for managing sessions
# # st.sidebar.markdown("### 🗂️ Chat Sessions")

# # # Get list of existing sessions
# # session_names = list(st.session_state.sessions.keys())

# # Add "New Chat" option on top
# # selected_session = st.sidebar.radio(
# #     "Select a session",
# #     ["New Chat"] + session_names,
# #     index=0,
# #     label_visibility="collapsed"
# # )

# # # Update active session
# # st.session_state.active_session = selected_session

# # # Create new session
# # if st.sidebar.button("➕ New Chat"):
# #     new_name = f"Chat {len(session_names) + 1}"
# #     st.session_state.sessions[new_name] = []
# #     st.session_state.active_session = new_name
# #     st.rerun()

# # # Load/init chat for current session
# # initialize_chat(model_name, st.session_state.active_session)

# # # Show chat interface
# # display_chat_ui()




# # main.py

# import streamlit as st
# from app.ui import display_chat_ui
# from app.chatbot import initialize_chat

# st.set_page_config(page_title="💬 Gemini Chatbot", layout="centered")

# # ✅ Initialize session state only once
# if "sessions" not in st.session_state:
#     st.session_state.sessions = {"New Chat": []}

# if "active_session" not in st.session_state:
#     st.session_state.active_session = "New Chat"

# if "chat_session" not in st.session_state:
#     st.session_state.chat_session = "New Chat"

# if "chat_model" not in st.session_state:
#     st.session_state.chat_model = "gemini-1.5-flash"

# # ✅ SIDEBAR
# st.sidebar.title("⚙️ Chat Control")

# # 🎛️ Model dropdown
# model_name = st.sidebar.selectbox(
#     "Select Gemini Model",
#     options=["gemini-1.5-flash", "gemini-1.5-flash-8b","gemini-2.0-flash","gemini-2.0-flash-thinking-exp-01-21"],
#     index=0
# )



# if st.sidebar.button("➕ New Chat"):
#     new_name = f"Chat {len(st.session_state.sessions) + 1}"

#     # 1️⃣ Create a clean session
#     st.session_state.sessions[new_name] = []

#     # 2️⃣ Switch active session
#     st.session_state.active_session = new_name
#     st.session_state.chat_session = new_name

#     # 3️⃣ Reinitialize empty chat
#     from app.chatbot import initialize_empty_chat
#     st.session_state.chat = initialize_empty_chat()

#     # 4️⃣ Refresh UI
#     st.rerun()

# # 🗂️ Session list (AFTER new chat logic)
# session_names = list(st.session_state.sessions.keys())

# selected_session = st.sidebar.radio(
#     "Select a session",
#     session_names,
#     index=session_names.index(st.session_state.active_session)
# )

# # ↩️ Handle session change
# if selected_session != st.session_state.active_session:
#     st.session_state.active_session = selected_session
#     st.session_state.chat_session = selected_session
#     st.rerun()



# # ✏️ Rename session
# with st.sidebar.expander("✏️ Rename Chat"):
#     rename_from = st.selectbox("Select session to rename", session_names)
#     new_name = st.text_input("New name")

#     if st.button("Rename") and new_name and new_name not in st.session_state.sessions:
#         st.session_state.sessions[new_name] = st.session_state.sessions.pop(rename_from)
#         if st.session_state.active_session == rename_from:
#             st.session_state.active_session = new_name
#             st.session_state.chat_session = new_name
#         st.rerun()

# # 🗑️ Select session to delete
# with st.sidebar.expander("🗑️ Delete Session"):
#     del_session = st.selectbox("Select a session to delete", st.session_state.sessions.keys())
#     if st.button("Delete", key="delete_session_btn"):
#         del st.session_state.sessions[del_session]

#         # If deleting the active session → open a fresh chat
#         if st.session_state.active_session == del_session:
#             new_name = f"Chat {len(st.session_state.sessions) + 1}"
#             st.session_state.sessions[new_name] = []
#             st.session_state.active_session = new_name
#             st.session_state.chat_session = new_name

#             from app.chatbot import initialize_empty_chat
#             st.session_state.chat = initialize_empty_chat()
        
#         st.rerun()


# # 🔁 Initialize chat logic
# initialize_chat(model_name, st.session_state.chat_session)

# # 🧠 Save selected model
# st.session_state.chat_model = model_name

# # 💬 Show UI
# display_chat_ui()




import streamlit as st
from app.chatbot import initialize_chat
from app.ui import sidebar, display_chat_ui

st.set_page_config(page_title="Mini Gemini Chatbot", page_icon="💬")

sidebar()

# Initialize chat object
if "chat" not in st.session_state or st.session_state.active_session == "New Chat":
    initialize_chat()

st.title("💬 Gemini Mini Chatbot")

display_chat_ui()

# User input
user_input = st.chat_input("Ask anything...")
if user_input:
    session_key = st.session_state.active_session
    if session_key not in st.session_state.sessions:
        st.session_state.sessions[session_key] = []

    # Save user message
    st.session_state.sessions[session_key].append({
        "role": "user",
        "text": user_input,
        "model": st.session_state.chat_model
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Send to Gemini
    response = st.session_state.chat.send_message(user_input)

    # Save assistant response
    st.session_state.sessions[session_key].append({
        "role": "assistant",
        "text": response.text,
        "model": st.session_state.chat_model
    })

    with st.chat_message("assistant"):
        st.markdown(f"**Model: {st.session_state.chat_model}**\n\n{response.text}")
