# 📄 PDF Chat AI (RAG-based)

🚀 Upload any PDF and ask questions — get intelligent answers using AI.


## 🔥 Features
* 📂 Upload multiple PDFs
* 🤖 Ask questions from documents
* 🧠 Uses RAG (Retrieval-Augmented Generation)
* ⚡ Fast similarity search using FAISS
* 💬 Clean chat interface (Streamlit)
* 🌐 Deployed on cloud


## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **Backend**: FastAPI
* **AI Model**: Groq (LLaMA 3)
* **Embeddings**: Sentence Transformers
* **Vector DB**: FAISS
* **Containerization**: Docker


## ⚙️ How It Works

1. Upload PDF 📄
2. Text is extracted
3. Converted into embeddings
4. Stored in FAISS index
5. User query → similarity search
6. Context + question → AI generates answer


## 📸 Demo

👉 Upload PDF → Ask Question → Get Answer



---

## 🚀 Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/pdf-chat.git
cd pdf-chat
docker compose up --build
```

---

## 🌐 Live Demo

👉 https://your-frontend-url.onrender.com

---

## 🔐 Environment Variables

Create `.env` file:

```env
GROQ_API_KEY=your_api_key
```

---

## 💡 Example Questions

* What is AI?
* Summarize this document
* What are key points?

---

## 📈 Future Improvements

* ChatGPT-like UI
* Save chat history
* Multi-user support
* PDF highlighting

---

## 🤝 Contributing

Pull requests are welcome!

---
## ⭐ Support
If you like this project:

👉 Star ⭐ the repo
👉 Follow me on GitHub

---
