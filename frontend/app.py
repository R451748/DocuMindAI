import streamlit as st
import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL")

st.set_page_config(page_title="PDF Chat AI", layout="wide")

st.title("📄 DocuMind AI")

# Check backend URL
if not BACKEND_URL:
    st.error("BACKEND_URL is not configured")
    st.stop()

# Upload PDFs
files = st.file_uploader(
    "Upload PDFs",
    type="pdf",
    accept_multiple_files=True
)

if st.button("Process PDFs") and files:

    files_data = [
        ("files", (f.name, f, "application/pdf"))
        for f in files
    ]

    try:
        with st.spinner("Processing PDFs..."):

            res = requests.post(
                f"{BACKEND_URL}/upload",
                files=files_data,
                timeout=None
            )

            data = res.json()

            st.success(data["message"])

    except Exception as e:
        st.error(f"Backend upload error: {e}")

# Chat memory
if "chat" not in st.session_state:
    st.session_state.chat = []

query = st.text_input("Ask a question")

if query:

    try:
        with st.spinner("Generating answer..."):

            res = requests.get(
                f"{BACKEND_URL}/ask",
                params={"query": query},
                timeout=60
            )

            data = res.json()

            st.session_state.chat.append(("You", query))
            st.session_state.chat.append(("AI", data["answer"]))

            st.subheader("💡 Answer")
            st.write(data["answer"])

    except Exception as e:
        st.error(f"Backend error: {e}")

# Sidebar history
st.sidebar.title("Chat History")

for role, msg in st.session_state.chat:
    st.sidebar.write(f"**{role}:** {msg}")
