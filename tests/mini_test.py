# mini_test.py

from llm import generate_answer

answer = generate_answer(
    "What is Snowflake Schema?",
    "Snowflake Schema is a database design where dimension tables are normalized."
)

print(answer)