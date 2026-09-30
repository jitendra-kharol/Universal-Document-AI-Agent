from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from upload_document import docs
from create_chunks import chunks
from embedding_model import emb_model
from create_vectorestore import retriever


prompt=ChatPromptTemplate.from_template("""

You are a Document Assistant.

Your job is to answer the user's questions using ONLY the provided document content.

DOCUMENT CONTENT:
{context}

USER QUESTION:
{question}

Follow these rules strictly:

1. Answer the user's question using the provided document content.
2. Do not use outside knowledge or make up information.
3. If the user asks a normal conversational question such as:
   - "Hello"
   - "Hi"
   - "How are you?"
   - "Who are you?"
   
   you may respond normally and politely.

4. If the question is related to the document but the answer cannot be found in the provided document content, say:
   "I could not find the answer to your question in the provided document."

5. If the question is completely unrelated to the document, say:
   "I can only provide answers related to the provided document."

6. Do not answer questions outside the scope of the provided document.

7. Do not assume, guess, or invent information that is not present in the document.

8. Keep your answer clear, accurate, and concise.

9. If the document contains the answer, explain it directly based on the document content.

Answer:
"""
)

model = ChatHuggingFace(
    llm = HuggingFaceEndpoint(
        repo_id="openai/gpt-oss-120b"
    )
)

while True:
    user_input = input("YOU:")
    if user_input.lower()=="exit":
        print("BYE.....")
        break

    embed_query = emb_model.embed_query(user_input)

    docs =  retriever.invoke(user_input)

    context = "\n\n".join(
    [doc.page_content for doc in docs]
        )

    final_prompt = prompt.invoke(
    {
        "context" :context,
        "question": user_input
    }
    )

    response = model.invoke(final_prompt)
    print(response.content)

