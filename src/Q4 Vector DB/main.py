from utils import embed_documents, retrieve_similar
import psycopg2

def main():
    conn = psycopg2.connect(
        dbname="mydb",
        user="root",
        password="password",
        host="localhost",
        port=5432,
    )

    query = "Usia Pertanggungan"
    vectors = embed_documents([query])
    docs = retrieve_similar(conn, vectors[0])
    for i, doc in enumerate(docs, start=1):
        print(f"Rank {i} - Score: {doc['similarity']:.3f}")
        print(doc['payload']['content'])
        print()


if __name__ == "__main__":
    main()
