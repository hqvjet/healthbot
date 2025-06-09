from datasets import load_dataset
from langchain_core.documents import Document

from app.utils import configs

def load_document():
    """
    Load the document dataset and create a vector store.
    """
    # Load the configuration for the document
    doc_config = configs['document']

    ds1 = load_dataset(doc_config['dataset1'])['train']


    ids = []
    docs = []

    for i in range(len(ds1)):
        document = Document(
            page_content=f'Question: {ds1[i]['question']}, Answer: {ds1[i]['answer']}',
            metadata={
                'id': str(i)
            }
        )
        ids.append(str(i))
        docs.append(document)

    return ids, docs



