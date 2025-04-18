import streamlit as st

MODEL_INFO = {
    "gemini-1.5-flash": "Lightweight, fast response model (1.5).",
    "gemini-1.5-flash-8b": "8-billion parameter flash variant.",
    "gemini-2.0-flash": "Latest 2.0 fast generation model.",
    "gemini-2.0-flash-thinking-exp-01-21": "Experimental version with reasoning."
}


def sidebar():
    st.sidebar.title("🧠 Chat Sessions")

    if "sessions" not in st.session_state:
        st.session_state.sessions = {}
        st.session_state.active_session = "New Chat"

    if "chat_model" not in st.session_state:
        st.session_state.chat_model = "gemini-1.5-flash"

    # Select session
    for name in list(st.session_state.sessions.keys()):
        if st.sidebar.button(name, key=f"select_{name}"):
            st.session_state.active_session = name

    # New Chat
    if st.sidebar.button("➕ New Chat"):
        # Ensure unique name
        base_name = "Chat"
        index = 1
        while f"{base_name} {index}" in st.session_state.sessions:
            index += 1
        new_name = f"{base_name} {index}"
        st.session_state.sessions[new_name] = []
        st.session_state.active_session = new_name

    st.sidebar.markdown("---")

    # Rename / Delete
    with st.sidebar.expander("📝 Manage Sessions"):
        if st.session_state.sessions:
            selected = st.selectbox("Select session", list(st.session_state.sessions.keys()), key="manage_select")

            # Rename
            new_name = st.text_input("Rename to", value=selected, key="rename_input")
            if st.button("✏️ Rename"):
                if new_name and new_name != selected:
                    # Avoid name collision
                    if new_name in st.session_state.sessions:
                        st.warning("Name already exists!")
                    else:
                        st.session_state.sessions[new_name] = st.session_state.sessions.pop(selected)
                        if st.session_state.active_session == selected:
                            st.session_state.active_session = new_name
                        st.success(f"Renamed to: {new_name}")
                        st.rerun()

            # Delete
            if st.button("🗑️ Delete"):
                del st.session_state.sessions[selected]
                if st.session_state.active_session == selected:
                    # Switch to new or empty session
                    if st.session_state.sessions:
                        st.session_state.active_session = list(st.session_state.sessions.keys())[0]
                    else:
                        st.session_state.active_session = "New Chat"
                st.success(f"Deleted session: {selected}")
                st.rerun()

    st.sidebar.markdown("---")

    # Model selector
    st.sidebar.markdown("### 🔍 Select Model")
    selected_model = st.sidebar.selectbox(
        "Choose a Gemini model",
        list(MODEL_INFO.keys()),
        format_func=lambda x: f"{x} 🎛️"
    )
    st.session_state.chat_model = selected_model
    st.sidebar.info(MODEL_INFO[selected_model])

 


def display_chat_ui():
    session_key = st.session_state.active_session

    if session_key not in st.session_state.sessions:
        st.session_state.sessions[session_key] = []

    for msg in st.session_state.sessions[session_key]:
        with st.chat_message(msg["role"]):
            # Tooltip with model info on hover
            model_display = f"<div title='Model: {msg['model']}'>{msg['text']}</div>"
            st.markdown(model_display, unsafe_allow_html=True)
