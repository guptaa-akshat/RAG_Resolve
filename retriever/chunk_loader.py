def load_chunks(file_path="troubleshooting_chunks.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]