import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from docx import Document
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from utils.file_utils import save_chunks

def read_docx(file_path):
    document = Document(file_path)
    full_text = "\n".join([para.text for para in document.paragraphs if para.text.strip()])
    return full_text

def chunk_text(text, chunk_size=100, overlap=50):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

docx_file = "Troubleshooting_Guide.docx"
full_text = read_docx(docx_file)
chunks = chunk_text(full_text)

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embedding_model.encode(chunks, convert_to_numpy=True)

index = faiss.IndexFlatL2(384)
index.add(embeddings)

faiss.write_index(index, "troubleshooting_index.faiss")
save_chunks(chunks, "troubleshooting_chunks.txt")

print(f"Saved {len(chunks)} chunks.")