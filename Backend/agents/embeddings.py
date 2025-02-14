import os
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import JinaEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from transformers import AutoTokenizer
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
        
        # Add any remaining lines as the last chunk
        if current_chunk:
            chunks.append(''.join(current_chunk))
    
    return chunks

def process_chunks(chunks, embeddings_model, batch_size=5):
    """Process chunks into embeddings"""
    qdrant_points = []
    
    # Create progress bar
    pbar = tqdm.tqdm(total=len(chunks), desc="Processing embeddings")
    
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        
        try:
            # Generate embeddings for the batch
            batch_embeddings = embeddings_model.embed_documents(batch)
            
            # Create Qdrant points
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

def main():
    # Define paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "output.txt")
    collection_name = "documents"
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist.")
    
    # Split file into 20-line chunks
    print("Splitting document into 20-line chunks...")
    chunks = split_file_by_lines(file_path, lines_per_chunk=20)
    print(f"Created {len(chunks)} chunks")
    
    # Initialize Jina Embeddings
    embeddings_model = JinaEmbeddings(
        jina_api_key=os.getenv("JINA_API_KEY"),
        model_name="jina-embeddings-v2-base-en"
    )
    
    # Process chunks into embeddings
    print("Processing embeddings...")
    qdrant_points = process_chunks(chunks, embeddings_model)
    
    # Insert into Qdrant
    if qdrant_points:
        print("Inserting embeddings into Qdrant...")
        
        
        # Insert in smaller batches
        batch_size = 100
        for i in range(0, len(qdrant_points), batch_size):
            batch = qdrant_points[i:i + batch_size]
            qdrant.upsert(collection_name=collection_name, points=batch)
            print(f"Inserted batch {i//batch_size + 1}/{len(qdrant_points)//batch_size + 1}")
    
    print("Process completed successfully!")

if __name__ == "__main__":
    main()