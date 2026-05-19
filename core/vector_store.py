import chromadb
from config import CHROMA_PATH, CHROMA_COLLECTION, TOP_K_RESULTS

client = chromadb.PersistentClient(path=CHROMA_PATH)


def get_or_create_collection():
    return client.get_or_create_collection(name=CHROMA_COLLECTION)


def index_chunks(chunks: list[dict], embeddings: list[list[float]]):
    collection = get_or_create_collection()
    collection.add(
        ids        = [c["id"]   for c in chunks],
        documents  = [c["text"] for c in chunks],
        embeddings = embeddings,
        metadatas  = [c["metadata"] for c in chunks]
    )


def search(query_embedding: list[float]) -> list[str]:
    collection = get_or_create_collection()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=TOP_K_RESULTS
    )
    return results["documents"][0]


def delete_collection():
    try:
        client.delete_collection(name=CHROMA_COLLECTION)
    except Exception:
        pass