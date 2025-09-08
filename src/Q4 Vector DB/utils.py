from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
import json
import psycopg2
import numpy as np
from typing import Any


load_dotenv()


def parse_pdf(file_path: str) -> list[str]:
    """
    Uses LangChain's PDF loader to extract and normalize text.
    Returns a list of documents (one per page).
    """
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return [doc.page_content for doc in docs]


def parse_documents(raw_texts: list[str]) -> list[str]:
    """
    Takes raw text inputs and returns a list of parsed documents (strings).
    In real use, you might add PDF, HTML, or DOCX loaders here.
    """
    # For simplicity, treat each string as one document
    return [text.strip() for text in raw_texts if text.strip()]


def chunk_documents(
    documents: list[str], chunk_size: int = 500, chunk_overlap: int = 50
) -> list[str]:
    """
    Splits documents into smaller overlapping chunks for embedding.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " ", ""],
    )
    chunks: list[str] = []
    for doc in documents:
        chunks.extend(splitter.split_text(doc))
    return chunks


def embed_documents(
    chunks: list[str], model: str = "gemini-embedding-001", dimension: int = 768
) -> list[list[float]]:
    """
    Embeds chunks into vector representations using OpenAI embeddings.
    """
    embeddings = GoogleGenerativeAIEmbeddings(model=model)
    return embeddings.embed_documents(chunks, output_dimensionality=dimension)


def insert_embedding(conn, vectors: list[list[float]], payloads: list[str]):
    """
    Insert embeddings + payloads into the custom Postgres vector table.

    Args:
        conn: psycopg2 connection
        vectors: list of embeddings (list of floats)
        payloads: list of metadata dicts, same length as vectors
    """
    if len(vectors) != len(payloads):
        raise ValueError("Vectors and payloads must have the same length")
    
    

    with conn.cursor() as cur:
        for vec, payload in zip(vectors, payloads):
            norm = float(np.linalg.norm(vec))
            cur.execute(
                """
                INSERT INTO vectors (vec, norm, payload)
                VALUES (%s, %s, %s)
                """,
                (vec, norm, json.dumps({"content": payload})),
            )
    conn.commit()

def retrieve_similar(
    conn,
    query_vector: list[float],
    topk: int = 5
) -> list[dict[str, Any]]:
    """
    Calls the custom Postgres function `search_vectors` to retrieve
    the most similar embeddings.
    
    Args:
        conn: psycopg2 connection
        query_vec: list of floats (embedding of query)
        topk: number of results to return
    
    Returns:
        List of dicts with id, payload, and similarity score
    """
    with conn.cursor() as cur:
        cur.execute(
            "SELECT * FROM search_vectors(ARRAY[%s]::float8[], %s);",
            (query_vector, topk)
        )
        rows = cur.fetchall()
    
    results = []
    for row in rows:
        item_id, payload, similarity = row
        results.append({
            "id": item_id,
            "payload": payload,
            "similarity": similarity
        })
    return results


# Example usage
if __name__ == "__main__":
    raw_docs = parse_pdf("./PRUFuture-Brosur.pdf")

    docs = parse_documents(raw_docs)
    chunks = chunk_documents(docs, chunk_size=128, chunk_overlap=10)[:32]

    vectors = embed_documents(chunks)

    conn = psycopg2.connect(
        dbname="mydb",
        user="root",
        password="password",
        host="localhost",
        port=5432,
    )
    insert_embedding(conn, vectors, chunks)
