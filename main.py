from models.classifier import classify_query
from retriever.chunk_loader import load_chunks
from retriever.faiss_retriever import search_faiss
from db.provider_query import get_provider_info
from utils.env_loader import *  # Ensures .env is loaded

def handle_query(query):
    query_type = classify_query(query)
    if query_type == "troubleshooting":
        chunks = load_chunks()
        return search_faiss(query, chunks)
    elif query_type == "provider_info":
        return get_provider_info()
    else:
        return "Couldn't classify query."

if __name__ == "__main__":
    user_query = input("Enter your query: ")
    result = handle_query(user_query)
    print("Response:", result)
