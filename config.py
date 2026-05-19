import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

EMBEDDING_MODEL = "models/gemini-embedding-001"
CHAT_MODEL      = "gemini-2.5-flash-lite"

CHUNK_SIZE    = 500   
CHUNK_OVERLAP = 50   

TOP_K_RESULTS = 3     

CHROMA_PATH       = "chroma_store"        
CHROMA_COLLECTION = "pdf_chunks"

SYSTEM_INSTRUCTION = (
    "You are a helpful assistant. Answer the user's question using ONLY "
    "the context provided below. If the answer is not in the context, say "
    "'I could not find that information in the document.' Do not make anything up."
)