from rag import (
    load_pdf,
    chunk_text,
    build_faiss_index,
    search_faiss
)

text = load_pdf("data/Data Modelling.pdf")

chunks = chunk_text(text)

index, embeddings = build_faiss_index(chunks)

results = search_faiss(
    "What is Snowflake Schema?",
    index,
    chunks
)

print("\nRetrieved Chunks:\n")

for i, chunk in enumerate(results, start=1):
    print(f"\nChunk {i}:")
    print(chunk[:300])