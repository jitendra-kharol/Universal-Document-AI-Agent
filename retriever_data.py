# retrieve_data.py

from dotenv import load_dotenv
load_dotenv()

from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore

from embedding_model import emb_model

import os

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

vector_store = QdrantVectorStore(
    Client=client,
    embedding=emb_model,
    collection_name="universal_document_ai"
)

final_retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)