# create_vectorestore.py

from dotenv import load_dotenv
load_dotenv()

from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore

from embedding_model import emb_model
from create_chunks import chunks

import os

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

vector_store = QdrantVectorStore(
    client=client,
    embedding=emb_model,
    collection_name="universal_document_ai"
)

vector_store.add_documents(chunks)

print("Documents successfully stored in Qdrant!")

retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)