from rag import (
    load_pdf,
    chunk_text,
    build_faiss_index,
    rag_answer
)

text = load_pdf("data/Data Modelling.pdf")

chunks = chunk_text(text)

index, embeddings = build_faiss_index(chunks)

input("Press Enter to continue...")

answer = rag_answer(
    "What is Snowflake Schema?",
    index,
    chunks
)

print(answer)