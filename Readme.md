# Live link: [Click Here](https://mini-chat-bot.streamlit.app/)

gemini_chatbot/
│
├── app/                        # Core app logic
│   ├── __init__.py
│   ├── chatbot.py              # Gemini chat logic
│   └── ui.py                   # UI components using Streamlit
│
├── .streamlit/
│   └── secrets.toml            # API key (Gemini)
│
├── main.py                     # Entry point to run the Streamlit app
├── requirements.txt            # Python dependencies
└── README.md                   # Project overview



Mini_chatbot/
│
├── app/
│   ├── chatbot.py      ← logic for Gemini chat init
│   └── ui.py           ← chat interface & chat history
│
├── main.py             ← full logic: UI + session management
├── requirements.txt
└── .streamlit/
    └── secrets.toml
