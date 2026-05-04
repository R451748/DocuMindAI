import streamlit as st
import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:8000")

st.set_page_config(page_title="PDF Chat AI", layout="wide")

st.title("📄 PDF Chat (Lightweight AI)")

# Upload PDFs
files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)

if st.button("Process PDFs") and files:
    files_data = [("files", (f.name, f, "application/pdf")) for f in files]

    try:
        res = requests.post(f"{BACKEND_URL}/upload", files=files_data)
        st.success(res.json()["message"])
    except:
        st.error("Backend not reachable")

# Chat memory
if "chat" not in st.session_state:
    st.session_state.chat = []

query = st.text_input("Ask a question")

if query:
    try:
        res = requests.get(f"{BACKEND_URL}/ask", params={"query": query})
        data = res.json()

        st.session_state.chat.append(("You", query))
        st.session_state.chat.append(("AI", data["answer"]))

        st.subheader("💡 Answer")
        st.write(data["answer"])


    except:
        st.error("Backend is not running!")

# Sidebar history
st.sidebar.title("Chat History")
for role, msg in st.session_state.chat:
    st.sidebar.write(f"**{role}:** {msg}")