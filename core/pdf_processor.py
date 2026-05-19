import pypdf
from config import CHUNK_SIZE, CHUNK_OVERLAP


def extract_text(file) -> str:
    reader = pypdf.PdfReader(file)
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def split_into_chunks(text: str) -> list[dict]:
    chunks = []
    start = 0
    index = 0

    while start < len(text):
        end = start + CHUNK_SIZE
        chunk_text = text[start:end].strip()

        if chunk_text:
            chunks.append({
                "id":   f"chunk_{index}",
                "text": chunk_text,
                "metadata": {"chunk_index": index}
            })
            index += 1

        start += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks


def process_pdf(file) -> list[dict]:
    text = extract_text(file)
    return split_into_chunks(text)