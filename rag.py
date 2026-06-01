from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import ollama
import faiss
import numpy as np
from llm import generate_answer


def load_pdf(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text

def chunk_text(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    return chunks

def create_embedding(text):

    response = ollama.embeddings(
        model="nomic-embed-text",
        prompt=text
    )

    return response["embedding"]

def build_faiss_index(chunks):

    embeddings = []

    for chunk in chunks:
        embedding = create_embedding(chunk)
        embeddings.append(embedding)

    embeddings = np.array(
        embeddings,
        dtype=np.float32
    )

    dimension = len(embeddings[0])

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index, embeddings

def search_faiss(
    query,
    index,
    chunks,
    k=3
):

    query_embedding = create_embedding(query)

    query_embedding = np.array(
        [query_embedding],
        dtype=np.float32
    )

    distances, indices = index.search(
        query_embedding,
        k
    )

    results = []

    for idx in indices[0]:
        results.append(
            chunks[idx]
        )

    return results

def rag_answer(question, index, chunks):

    retrieved_chunks = search_faiss(
    question,
    index,
    chunks,
    k=3
    )

    context = "\n\n".join(retrieved_chunks)

    # print("Context Length:", len(context))
    # print(context[:1000])

    answer = generate_answer(
        question,
        context
    )

    return answer