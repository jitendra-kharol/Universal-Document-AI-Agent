# create_chunk.py

from langchain_text_splitters import RecursiveCharacterTextSplitter
from upload_document import docs

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(docs)