from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_answer(question, context):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
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

Context:
{context}

Instructions:
- Use the context to answer the question.
- Summarize and explain in your own words.
- Do not copy large portions of the context.
- If the answer is not present, say so.
"""
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content