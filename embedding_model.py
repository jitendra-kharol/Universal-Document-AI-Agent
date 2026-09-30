# create_embedding.py

from langchain_huggingface import HuggingFaceEmbeddings

emb_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-MiniLM-L3-v2"
)