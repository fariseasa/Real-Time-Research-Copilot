from rag import load_pdf, chunk_text

text = load_pdf("data/Data Modelling.pdf")

chunks = chunk_text(text)

print("Number of chunks:", len(chunks))

print("\nFirst chunk:\n")
print(chunks[0])

print("Characters in first chunk:", len(chunks[0]))
print("Characters in second chunk:", len(chunks[1]))