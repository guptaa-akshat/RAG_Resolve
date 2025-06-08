import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("troubleshooting_index.faiss")

def search_faiss(query, chunks):
    query_embedding = embedding_model.encode(query, convert_to_numpy=True)
    distances, indices = index.search(np.array([query_embedding], dtype=np.float32), k=1)
    if indices[0][0] != -1 and indices[0][0] < len(chunks):
        return chunks[indices[0][0]]
    return "No troubleshooting information found."
