from ollama import chat


def generate_answer(question, search_results):

    response = chat(
        model="llama3.1:8b",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful research assistant."
            },
            {
                "role": "user",
                "content": f"""
Question:
{question}

Search Results:
{search_results}

Using only the search results provided,
answer the question clearly.
"""
            }
        ]
    )

    return response["message"]["content"]