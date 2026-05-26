from auth import login
import streamlit as st
from pypdf import PdfReader
import google.generativeai as genai
from dotenv import load_dotenv
import os
from vector_db import create_vector_store
from encryption import encrypt_file
from datetime import datetime
import glob

# ENV
load_dotenv()

genai.configure(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# Logging
def log_event(event):

    os.makedirs(
        "logs",
        exist_ok=True
    )

    with open(
        "logs/activity.log",
        "a",
        encoding="utf-8"
    ) as f:

        f.write(
            f"{datetime.now()} - {event}\n"
        )


# Extract PDF text
def extract_text(file):

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:

            text += page_text

    return text


# SESSION
if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

if "chat_history" not in st.session_state:

    st.session_state.chat_history = []


# LOGIN
if not st.session_state.logged_in:

    st.title(
        "🔐 Secure Login"
    )

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "Login"
    ):

        if login(
            username,
            password
        ):

            st.session_state.logged_in = True

            log_event(
                f"{username} logged in"
            )

            st.success(
                "Login successful"
            )

            st.rerun()

        else:

            log_event(
                "Failed login"
            )

            st.error(
                "Invalid credentials"
            )

    st.stop()


# MAIN UI
st.title(
    "🔐 Secure GenAI Enterprise Document Assistant"
)

# DASHBOARD
col1, col2 = st.columns(2)

uploads_count = len(
    glob.glob(
        "uploads/*"
    )
)

col1.metric(
    "Encrypted Files",
    uploads_count
)

col2.metric(
    "Chat Messages",
    len(
        st.session_state.chat_history
    )
)


# Logout
if st.button(
    "Logout"
):

    st.session_state.logged_in = False

    st.rerun()


# Multi upload
uploaded_files = st.file_uploader(
    "Upload PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

all_text = ""

if uploaded_files:

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    for uploaded in uploaded_files:

        file_bytes = uploaded.read()

        encrypted = encrypt_file(
            file_bytes
        )

        path = (
            f"uploads/{uploaded.name}.enc"
        )

        with open(
            path,
            "wb"
        ) as f:

            f.write(
                encrypted
            )

        log_event(
            f"Uploaded {uploaded.name}"
        )

        uploaded.seek(0)

        all_text += extract_text(
            uploaded
        )

    st.success(
        "Encrypted files stored"
    )


question = st.text_input(
    "Ask documents"
)

if question and all_text:

    log_event(
        f"Question: {question}"
    )

    db = create_vector_store(
        all_text
    )

    docs = db.similarity_search(
        question,
        k=3
    )

    context = "\n".join(
        [
            d.page_content
            for d in docs
        ]
    )

    prompt = f"""
Context:

{context}

Question:

{question}

Answer only using context.
"""

    response = model.generate_content(
        prompt
    )

    answer = response.text

    st.write(
        answer
    )

    st.session_state.chat_history.append(
        (
            question,
            answer
        )
    )


# Chat history
st.subheader(
    "Chat History"
)

for q, a in st.session_state.chat_history:

    st.write(
        f"Q: {q}"
    )

    st.write(
        f"A: {a}"
    )


# Log viewer
if st.button(
    "View Logs"
):

    with open(
        "logs/activity.log",
        "r",
        encoding="utf-8"
    ) as f:

        st.text(
            f.read()
        )