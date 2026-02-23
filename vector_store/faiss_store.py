import faiss
import numpy as np

# Create FAISS index
def create_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

# 🔥 THIS WAS MISSING — add this function
def search_index(index, query_embedding, chunks, k=3):
    query_embedding = np.array([query_embedding]).astype("float32")
    distances, indices = index.search(query_embedding, k)

    results = []
    for i in indices[0]:
        results.append(chunks[i])

    return results