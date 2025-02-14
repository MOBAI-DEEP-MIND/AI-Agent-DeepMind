import os
from dotenv import load_dotenv
from langchain_community.embeddings import JinaEmbeddings
from qdrant_client.models import PointStruct
import tqdm
from vector_db import qdrant  

# Load environment variables
load_dotenv()

def split_file_by_lines(file_path, lines_per_chunk=20):
    """Split the file into chunks of specified number of lines"""
    chunks = []
    with open(file_path, 'r') as file:
        current_chunk = []
        for line in file:
            current_chunk.append(line)
            if len(current_chunk) >= lines_per_chunk:
                chunks.append(''.join(current_chunk))
                current_chunk = []
        
        if current_chunk:  # Add any remaining lines
            chunks.append(''.join(current_chunk))
    
    return chunks

def embed_query(query: str, embeddings_model) -> list:
    """Embed a single query string using the provided embeddings model"""
    try:
        return embeddings_model.embed_query(query)
    except Exception as e:
        print(f"Error embedding query: {str(e)}")
        return None

def search_similar_chunks(query_embedding, collection_name: str, limit: int = 5):
    """Search for similar chunks using the query embedding"""
    if query_embedding is None:
        return []
    
    try:
        return qdrant.search(
            collection_name=collection_name,
            query_vector=query_embedding,
            limit=limit
        )
    except Exception as e:
        print(f"Error searching similar chunks: {str(e)}")
        return []

def process_chunks(chunks, embeddings_model, batch_size=5):
    """Process chunks into embeddings for storage in Qdrant"""
    qdrant_points = []
    pbar = tqdm.tqdm(total=len(chunks), desc="Processing embeddings")
    
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        
        try:
            batch_embeddings = embeddings_model.embed_documents(batch)
            for j, embedding in enumerate(batch_embeddings):
                qdrant_points.append(
                    PointStruct(
                        id=i + j,
                        vector=embedding,
                        payload={"text": batch[j]}
                    )
                )
            pbar.update(len(batch))
        except Exception as e:
            print(f"Error processing batch {i//batch_size}: {str(e)}")
            continue
    
    pbar.close()
    return qdrant_points

def main(query):
    collection_name = "documents"
    file_path = "output.txt"  # Ensure this exists

    # Initialize Jina Embeddings
    embeddings_model = JinaEmbeddings(
        jina_api_key=os.getenv("JINA_API_KEY"),
        model_name="jina-embeddings-v2-base-en"
    )

    # **Step 1: Process and store chunks**
    # print("Splitting file into chunks...")
    # chunks = split_file_by_lines(file_path)

    # print("Processing embeddings...")
    # qdrant_points = process_chunks(chunks, embeddings_model)

    # if qdrant_points:
    #     print("Inserting embeddings into Qdrant...")
    #     batch_size = 100
    #     for i in range(0, len(qdrant_points), batch_size):
    #         batch = qdrant_points[i:i + batch_size]
    #         qdrant.upsert(collection_name=collection_name, points=batch)
    #         print(f"Inserted batch {i//batch_size + 1}/{len(qdrant_points)//batch_size + 1}")

    # **Step 2: Search with query (no storing of query)**
    print("Embedding query...")
    query_embedding = embed_query(query, embeddings_model)
    
    if query_embedding:
        similar_chunks = search_similar_chunks(query_embedding, collection_name)
        for i, result in enumerate(similar_chunks, 1):
            # print(f"\nResult {i}:")
            pass
            # print(f"Text: {result.payload['text']}")
            # print(f"Similarity Score: {result.score}")

    print("Process completed successfully!")
    return similar_chunks
if __name__ == "__main__":
    main("Im searching for a book that talks about thriller/suspense genre")
