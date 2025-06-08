from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
import os

from utils import config
from data.document import load_document

doc_config = config['document']

def create_vector_store():
    """
    Create a vector store from the document dataset.
    """

    if not os.path.exists(doc_config['db_location']):
        os.makedirs(doc_config['db_location'])

    embeddings = OllamaEmbeddings(model=doc_config['model'])
    idx, docs = load_document()

    vector_store = Chroma(
        collection_name="vi-medical-qa",
        persist_directory=doc_config['db_location'],
        embedding_function=embeddings,
    )

    print("Creating vector store...")
    batch_size = 5451
    for i in range(0, len(docs), batch_size):
        vector_store.add_documents(documents=docs[i:i + batch_size], ids=idx[i:i + batch_size])
    print("Vector store created and saved.")

def load_retriever():
    vector_store = Chroma(
        collection_name="vi-medical-qa",
        persist_directory=doc_config['db_location'],
        embedding_function=OllamaEmbeddings(model=doc_config['model']),
    )
    retriver = vector_store.as_retriever(search_kwargs={"k": 3})
    return retriver