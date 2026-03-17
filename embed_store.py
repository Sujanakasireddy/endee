import numpy as np

with open("data/documents.txt") as f:
    docs = f.readlines()

vector_store = []

for doc in docs:

    # simple vector representation
    vector = np.random.rand(10)

    vector_store.append({
        "text": doc,
        "vector": vector
    })

np.save("vector_store.npy", vector_store)

print("Vectors stored successfully")