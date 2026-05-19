import google.generativeai as genai
from config import GEMINI_API_KEY, CHAT_MODEL, SYSTEM_INSTRUCTION
from core.embedder import embed_query
from core.vector_store import search

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(
    model_name=CHAT_MODEL,
    system_instruction=SYSTEM_INSTRUCTION
)


def ask(question: str) -> str:
    query_embedding = embed_query(question)
    chunks          = search(query_embedding)
    context         = "\n\n".join(chunks)
    prompt          = f"Context:\n{context}\n\nQuestion: {question}"
    response        = model.generate_content(prompt)
    return response.text