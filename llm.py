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
- Use the provided context to answer the question.
- Combine information from multiple sources when needed.
- For rankings, lists, or comparisons, synthesize the information into a complete answer.
- Be clear, concise, and informative.
- If information is incomplete, provide the best answer possible and mention any limitations.
"""
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content