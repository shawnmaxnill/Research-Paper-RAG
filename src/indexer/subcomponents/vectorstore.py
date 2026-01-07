'''
Embeddings for words using FAISS similarity search
'''

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os


class VectorIndexer:

    def __init__(self, index_path = None):
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

        if index_path is None:
            # Resolve project root dynamically
            base_dir = os.path.dirname(os.path.abspath(__file__))  # subcomponents/
            src_dir = os.path.dirname(os.path.dirname(base_dir))   # src/
            project_root = os.path.dirname(src_dir)                # paper_exp/

            index_path = os.path.join(project_root, "data", "vecstore")

        self.index_path = index_path
        self.vectorstore = None

    def build(self, documents):
        self.vectorstore = FAISS.from_documents(documents, self.embeddings)

    def save(self):
        self.vectorstore.save_local(self.index_path)

    def load(self):
        self.vectorstore = FAISS.load_local(self.index_path, self.embeddings)
    
    def get_retriever(self):
        return self.vectorstore.as_retriever()