from ollama import chat

def generate_answer(question, context):

    response = chat(
        model="llama3.1:8b",
        messages=[
            {
    "role": "user",
    "content": f"""
You are answering questions based on retrieved document context.

Question:
{question}

Context:
{context}

Instructions:
- Use the context to answer the question.
- Do not copy large portions of the context.
- Summarize and explain in your own words.
- If the answer is not in the context, say so.

Answer:
"""
}
        ]
    )

    return response["message"]["content"]