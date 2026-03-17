import numpy as np

vector_store = np.load("vector_store.npy", allow_pickle=True)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search(query):

    query_vector = np.random.rand(10)

    scores = []

    for item in vector_store:

        similarity = cosine_similarity(item["vector"], query_vector)

        scores.append((item["text"], similarity))

    scores.sort(key=lambda x: x[1], reverse=True)

    return scores[:3]