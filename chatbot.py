from search import search

def chatbot(query):

    results = search(query)

    context = ""

    for r in results:
        context += r[0] + "\n"

    response = f"""
Relevant Documents:

{context}

Answer based on retrieved context.
"""

    return response
