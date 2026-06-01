from search import web_search
from llm import generate_answer

question = input("Ask: ")

search_results = web_search(question)

answer = generate_answer(
    question,
    search_results["results"]
)

print("\nAnswer:\n")
print(answer)

print("\nSources:\n")

for i, item in enumerate(search_results["results"], start=1):
    print(f"{i}. {item['title']}")
    print(f"   {item['url']}")