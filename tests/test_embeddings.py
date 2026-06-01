from rag import create_embedding

embedding = create_embedding(
    "What is Snowflake Schema?"
)

print(type(embedding))
print(len(embedding))