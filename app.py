import psycopg2
from embedding_util import generate_embeddings

def run():

    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        user="myuser",
        password="mypassword",
        host="localhost",
        port=5432,  # The port you exposed in docker-compose.yml
        database="mydb"
    )

    # Create a cursor to execute SQL commands
    cur = conn.cursor()

    try:
        sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "Machine learning models have become increasingly important in data analysis.",
            "A stitch in time saves nine.",
            "It was a bright cold day in April, and the clocks were striking thirteen.",
            "Artificial intelligence is transforming industries worldwide.",
            "The rain in Spain stays mainly in the plain.",
            "The cat sat on the mat.",
            "Natural language processing enables computers to understand human language.",
            "Early to bed and early to rise makes a man healthy, wealthy, and wise.",
            "The dog chased the cat around the garden."
        ]

        # Insert sentences into the items table
        for sentence in sentences:
            embedding = generate_embeddings(sentence)
            cur.execute(
                "INSERT INTO items (content, embedding) VALUES (%s, %s)",
                (sentence, embedding)
            )
            print(sentence, ":", embedding)

        print("############################")
        # Example query
        query = "Give me some content about machine learning"
        query_embedding = generate_embeddings(query)

        # Perform a cosine similarity search
        cur.execute(
            """SELECT id, content, 1 - (embedding <=> %s) AS cosine_similarity
               FROM items
               ORDER BY cosine_similarity DESC LIMIT 5""",
            (query_embedding,)
        )

        # Fetch and print the result
        print("Query:", query)
        print("Most similar sentences:")
        for row in cur.fetchall():
            print(
                f"ID: {row[0]}, CONTENT: {row[1]}, Cosine Similarity: {row[2]}")

    except Exception as e:
        print("Error executing query", str(e))
    finally:
        # Close communication with the PostgreSQL database server
        cur.close()
        conn.close()

# This check ensures that the function is only run when the script is executed directly, not when it's imported as a module.
if __name__ == "__main__":
    run()
