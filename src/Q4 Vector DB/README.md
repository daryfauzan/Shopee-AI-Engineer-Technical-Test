# Custom Vector Database with Cosine Similarity Search

A lightweight Python implementation of a vector database using PostgreSQL for document embedding and cosine similarity search. This project demonstrates how to build a custom vector search system without relying on specialized vector databases like Pinecone or Weaviate.

## Features

- **PDF Document Processing**: Extract and parse text from PDF files using LangChain
- **Document Chunking**: Split large documents into smaller, overlapping chunks for better embedding
- **Vector Embeddings**: Generate embeddings using Google's Gemini embedding model
- **Custom PostgreSQL Vector Storage**: Store embeddings with metadata in PostgreSQL
- **Cosine Similarity Search**: Implement efficient similarity search using custom SQL functions
- **Dockerized Database**: Easy setup with Docker Compose

## Project Structure

```
.
├── main.py                 # Main application entry point
├── utils.py                # Core utilities for document processing and vector operations
├── vector_search.sql       # PostgreSQL schema and search functions
├── docker-compose.yaml     # Docker setup for PostgreSQL
├── pyproject.toml          # Python dependencies
└── README.md              # This file
```

## Prerequisites

- Python 3.11+
- Docker and Docker Compose
- Google AI API key (for Gemini embeddings)

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd q4-vector-db
   ```

2. **Install Python dependencies**
   ```bash
   pip install -e .
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   GOOGLE_API_KEY=your_google_ai_api_key_here
   ```

4. **Start the PostgreSQL database**
   ```bash
   docker-compose up -d
   ```

5. **Initialize the database schema**
   Connect to your PostgreSQL database and run the SQL commands from `vector_search.sql`:
   ```bash
   psql -h localhost -p 5432 -U root -d mydb -f vector_search.sql
   ```

## Usage

### Processing and Indexing Documents

The project includes utilities to process PDF documents and store their embeddings:

```python
from utils import parse_pdf, parse_documents, chunk_documents, embed_documents, insert_embedding
import psycopg2

# Parse PDF and create chunks
raw_docs = parse_pdf("./your-document.pdf")
docs = parse_documents(raw_docs)
chunks = chunk_documents(docs, chunk_size=500, chunk_overlap=50)

# Generate embeddings
vectors = embed_documents(chunks)

# Store in database
conn = psycopg2.connect(
    dbname="mydb", user="root", password="password",
    host="localhost", port=5432
)
insert_embedding(conn, vectors, chunks)
```

### Searching for Similar Documents

Use the main application to search for documents similar to your query:

```python
from utils import embed_documents, retrieve_similar
import psycopg2

# Connect to database
conn = psycopg2.connect(
    dbname="mydb", user="root", password="password",
    host="localhost", port=5432
)

# Search for similar documents
query = "Your search query here"
query_vector = embed_documents([query])[0]
results = retrieve_similar(conn, query_vector, topk=5)

# Display results
for i, doc in enumerate(results, start=1):
    print(f"Rank {i} - Score: {doc['similarity']:.3f}")
    print(doc['payload']['content'])
```

### Running the Example

The project includes a working example that searches for "Usia Pertanggungan":

```bash
python main.py
```

## Key Components

### Document Processing (`utils.py`)

- **`parse_pdf()`**: Extract text from PDF files
- **`chunk_documents()`**: Split documents into overlapping chunks
- **`embed_documents()`**: Generate vector embeddings using Gemini
- **`insert_embedding()`**: Store vectors and metadata in PostgreSQL
- **`retrieve_similar()`**: Search for similar documents using cosine similarity

### Database Schema (`vector_search.sql`)

The database uses a simple but effective schema:

```sql
CREATE TABLE vectors (
  id SERIAL PRIMARY KEY,
  vec FLOAT8[],           -- Vector embedding as array
  norm FLOAT8,            -- Pre-computed vector norm for efficiency
  payload JSONB           -- Document content and metadata
);
```

### Custom Search Function

A PostgreSQL function implements efficient cosine similarity search:

```sql
CREATE OR REPLACE FUNCTION search_vectors(qvec FLOAT8[], topk INT)
RETURNS TABLE (item_id INT, payload JSONB, similarity FLOAT8) AS $$
DECLARE
    qnorm FLOAT8;
BEGIN
    qnorm := sqrt((SELECT sum(x^2) FROM unnest(qvec) AS t(x)));

    RETURN QUERY
    SELECT v.id, v.payload, 
           (SELECT sum(x * y)
            FROM unnest(v.vec, qvec) AS t(x,y)) / (v.norm * qnorm) AS cosine_similarity
    FROM vectors v
    ORDER BY cosine_similarity DESC
    LIMIT topk;
END;
$$ LANGUAGE plpgsql;
```

## Configuration Options

### Embedding Parameters

- **Model**: `gemini-embedding-001` (768 dimensions)
- **Chunk Size**: 500 characters (adjustable)
- **Chunk Overlap**: 50 characters (adjustable)

### Database Connection

Default connection parameters (modify in your code):
- **Host**: localhost
- **Port**: 5432
- **Database**: mydb
- **User**: root
- **Password**: password

## Performance Considerations

- **Indexing**: Consider adding indexes on vector norms for large datasets
- **Batch Processing**: Process documents in batches for better memory efficiency
- **Connection Pooling**: Use connection pooling for production deployments
- **Chunking Strategy**: Adjust chunk size based on your document types and search requirements

## Limitations

- **Scalability**: This implementation is suitable for small to medium datasets
- **Vector Indexes**: Doesn't use specialized vector indexes (like HNSW)
- **Exact Search**: Performs exact cosine similarity (not approximate)
- **Single-threaded**: Processing is single-threaded

## Future Improvements

- Add support for other embedding models
- Implement approximate nearest neighbor search
- Add batch processing capabilities
- Include more document formats (DOCX, HTML, etc.)
- Add vector index optimization
- Implement query result caching

## Dependencies

- **LangChain**: Document processing and PDF loading
- **Google Generative AI**: Embedding generation
- **psycopg2**: PostgreSQL database adapter
- **NumPy**: Numerical operations
- **python-dotenv**: Environment variable management
