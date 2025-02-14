from vector_db import qdrant as client
from qdrant_client.models import PointStruct
from openai import AzureOpenAI
from typing import List, Union
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the Azure OpenAI client
client_azure = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)


#loading the data from the csv file

data = pd.read_csv('data_cleaned.csv')
texts = data['text']



def create_embeddings(
    texts: Union[str, List[str]],
    client: AzureOpenAI,
    model: str = "text-embedding-ada-002",
    batch_size: int = 100
) -> List[List[float]]:
    
    # Convert single string to list for consistent processing
    if isinstance(texts, str):
        texts = [texts]
    
    all_embeddings = []
    
    try:
        # Process in batches to handle large numbers of texts
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            
            response = client.embeddings.create(
                input=batch,
                model=model
            )
            
            # Extract embeddings from response
            batch_embeddings = [item.embedding for item in response.data]
            all_embeddings.extend(batch_embeddings)
            
        return all_embeddings
    
    except Exception as e:
        raise Exception(f"Failed to create embeddings: {str(e)}")



def insert_embeddings(data, collection_name, embeddings):
    # Prepare points (embeddings + metadata) for Qdrant
    points = [
        PointStruct(
            id=idx,  # Unique ID for each point
            vector=embedding.tolist(),  # Convert numpy array to list
            payload={"text": text}  # Metadata (e.g., original text)
        )
        for idx, (text, embedding) in enumerate(zip(texts, embeddings))
    ]

    # Upload points to Qdrant
    client.upsert(
        collection_name=collection_name,
        points=points
    )

def search(collection_name, query, top_k=5):

    # Embed the query
    query_embedding = create_embeddings([query])[0]

    # Search for similar points
    results = client.search(
        collection_name=collection_name,
        query=query_embedding.tolist(),
        top_k=top_k
    )

    return results

# Create embeddings for all texts
embeddings = create_embeddings(texts, client_azure)
print(f"Created {len(embeddings)} embeddings.")