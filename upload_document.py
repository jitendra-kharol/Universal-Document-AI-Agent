# upload_document.py

from langchain_community.document_loaders import PyPDFLoader

file_path = "D:/Universal Document AI Agent/document/jitendra_kharol.pdf"

loader = PyPDFLoader(file_path)

docs = loader.load()