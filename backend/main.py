from fastapi import FastAPI, UploadFile
from rag import RAG
from groq import Groq
from PyPDF2 import PdfReader
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="PDF Chat API")

rag = RAG()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.get("/")
def health():
    return {"status": "API running"}

# -------- UPLOAD --------
@app.post("/upload")
async def upload(files: list[UploadFile]):
    try:
        all_text = []

        for file in files:
            pdf = PdfReader(file.file)
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    all_text.append(text)

        if not all_text:
            return {"message": "No readable text found"}

        rag.create_index(all_text)

        return {"message": "PDF processed successfully"}

    except Exception as e:
        return {"message": str(e)}

# -------- ASK --------
@app.get("/ask")
def ask(query: str):
    try:
        if rag.vectors is None:
            return {"answer": "Upload PDF first", "sources": []}

        context_chunks = rag.search(query)
        context = "\n".join(context_chunks)

        prompt = f"""
        Answer ONLY using the context below:

        {context}

        Question: {query}
        """

        response = client.chat.completions.create(
           model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )

        return {
            "answer": response.choices[0].message.content
            
        }

    except Exception as e:
        return {"answer": str(e), "sources": []}
