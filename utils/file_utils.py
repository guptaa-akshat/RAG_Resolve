def save_chunks(chunks, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(chunk + "\n")