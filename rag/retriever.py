import faiss
import pickle
from sentence_transformers import SentenceTransformer

import os
from rag.build_index import build_faiss_index

INDEX_PATH = "rag/index"
INDEX_FILE = f"{INDEX_PATH}/math.index"
CHUNKS_FILE = f"{INDEX_PATH}/chunks.pkl"

model = SentenceTransformer("all-MiniLM-L6-v2")

# Check if index exists, if not build it (Critical for Cloud Deployment)
if not os.path.exists(INDEX_FILE) or not os.path.exists(CHUNKS_FILE):
    print("⚠️ Index not found. Building it now from Knowledge Base...")
    build_faiss_index()

index = faiss.read_index(INDEX_FILE)

with open(CHUNKS_FILE, "rb") as f:
    chunks = pickle.load(f)


def retrieve_context(query, top_k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, top_k)

    return [chunks[i] for i in indices[0]]
