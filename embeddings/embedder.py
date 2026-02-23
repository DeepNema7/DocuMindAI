from sentence_transformers import SentenceTransformer

# Force local embedding model only
model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(chunks):
    if not chunks:
        return []
    embeddings = model.encode(chunks, convert_to_numpy=True)
    return embeddings
