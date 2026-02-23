import numpy as np

def search_index(index, query_embedding, chunks, top_k=2):
    query_embedding = np.array([query_embedding]).astype("float32")
    distances, indices = index.search(query_embedding, top_k)

    results = []
    for i in indices[0]:
        results.append(chunks[i])

    return results
