import google.generativeai as genai
from config import GEMINI_API_KEY, EMBEDDING_MODEL

genai.configure(api_key=GEMINI_API_KEY)


def embed_documents(texts: list[str]) -> list[list[float]]:
    result = []
    for text in texts:
        response = genai.embed_content(
            model=EMBEDDING_MODEL,
            content=text,
            task_type="retrieval_document"
        )
        result.append(response["embedding"])
    return result


def embed_query(text: str) -> list[float]:
    response = genai.embed_content(
        model=EMBEDDING_MODEL,
        content=text,
        task_type="retrieval_query"
    )
    return response["embedding"]