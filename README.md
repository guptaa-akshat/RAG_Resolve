# 🛠️ RAGResolve: AI-Powered Troubleshooting Assistant

RAGResolve is an intelligent Retrieval-Augmented Generation (RAG) system designed to assist users in resolving troubleshooting queries or retrieving service provider information.

---

## 🚀 Features

- 🔍 **Query Classification**: Uses Groq LLM to classify user queries into `troubleshooting` or `provider_info`.
- 🧠 **Semantic Search**: Retrieves the most relevant troubleshooting guidance using FAISS and sentence embeddings.
- 📄 **Document Processing**: Converts a troubleshooting DOCX guide into text chunks and embeds them for retrieval.
- 🗃️ **PostgreSQL Integration**: Retrieves structured provider data from a relational database.
- 🔐 **.env-Based Secrets**: Manages API keys and database credentials securely.
- 🧱 **Modular Structure**: Clean, scalable code architecture for production-ready deployment.

```bash
python main.py
```bash


Install Requirements
```bash
pip install -r requirements.txt
```bash



Environment Setup
Create a .env file with the following:
```bash
GROQ_API_KEY=your_groq_api_key
PG_DBNAME=DBNAME
PG_USER=DBUSER
PG_PASSWORD=PASSWORD
PG_HOST=localhost
PG_PORT=PORT
```bash
