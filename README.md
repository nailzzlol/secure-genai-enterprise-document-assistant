# 🔐 Secure GenAI Enterprise Document Assistant  
### RAG + Semantic Search + Encryption + Authentication

Secure GenAI Enterprise Document Assistant is an enterprise-grade AI solution built using **Python, Streamlit, Gemini API, FAISS, and LangChain**. The application enables secure document processing, contextual question answering, semantic search, encrypted storage, authentication, activity logging, and multi-document intelligence using **Retrieval-Augmented Generation (RAG)**.

---

## 🚀 Features

✅ Secure PDF Upload & Processing  
✅ Multi-Document Support  
✅ Retrieval-Augmented Generation (RAG)  
✅ Semantic Search using FAISS Vector Database  
✅ Gemini-powered Question Answering  
✅ Encrypted File Storage using Fernet Encryption  
✅ User Authentication System  
✅ Activity Logging & Monitoring  
✅ Dashboard Analytics  
✅ Chat History Management  
✅ Enterprise-style Architecture

---

## 🏗 Architecture

```text
PDF Upload
    ↓
Encryption (Fernet)
    ↓
Text Extraction
    ↓
Chunking
    ↓
FAISS Vector Store
    ↓
Semantic Retrieval
    ↓
Gemini API
    ↓
Context-Aware Response
```

---

## 🛠 Tech Stack

### Programming Language
- Python

### AI / GenAI
- Google Gemini API
- Retrieval-Augmented Generation (RAG)
- Semantic Search

### Frameworks & Libraries
- Streamlit
- LangChain
- FAISS
- Sentence Transformers
- PyPDF

### Security
- Fernet Encryption
- Authentication
- Activity Logging
- Secure File Handling

---

## 📂 Project Structure

```text
secure-genai-enterprise-document-assistant/
│── app.py
│── auth.py
│── encryption.py
│── vector_db.py
│── .env
│── .gitignore
│── requirements.txt
│── README.md
│── uploads/
│── logs/
```

---

## ⚙ Installation

Clone repository:

```bash
git clone https://github.com/your-username/secure-genai-enterprise-document-assistant.git
```

Move into project directory:

```bash
cd secure-genai-enterprise-document-assistant
```

Install dependencies:

```bash
py -m pip install -r requirements.txt
```

Run application:

```bash
py -m streamlit run app.py
```

---

## 🔑 Environment Variables

Create a `.env` file:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

⚠ Do NOT upload `.env` or `secret.key` files to GitHub.

---

## 📊 Sample Use Cases

- Enterprise document search
- Policy assistant
- Internal knowledge management
- Secure AI document assistant
- Document summarization
- Context-aware enterprise Q&A

---

## 📸 Screenshots

Add screenshots here:

- Login Page
- Dashboard
- PDF Upload
- Document Q&A
- Logs Viewer

---

## 🔮 Future Enhancements

- OCR Support
- Docker Deployment
- SQLite Database Integration
- Role-Based Access Control (RBAC)
- Sensitive Data Detection
- Cloud Deployment

---

## 👩‍💻 Author

Developed by **Nailah Khan**
