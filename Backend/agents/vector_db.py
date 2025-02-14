from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

# Connect to Qdrant Cloud
qdrant = QdrantClient(
     url="https://402934bb-9b8c-4e09-97e3-724b2fafe02e.us-east4-0.gcp.cloud.qdrant.io:6333",
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwiZXhwIjoxNzQ3MjU4Mjc0fQ.u0rOYGHRuXYStHshdJkYpwm6lk5AmpEw6ow749AlAa8"
)

# Get list of existing collections
collections = qdrant.get_collections().collections
collection_names = [c.name for c in collections]

# Check if 'books' collection exists
if "books" not in collection_names:
    print("Collection not found. Creating collection...")
    qdrant.recreate_collection(
        collection_name="books",
        vectors_config=VectorParams(size=768, distance=Distance.COSINE)
    )
    print("Collection 'books' created.")
else:
    print("Collection 'books' already exists.")