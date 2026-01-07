import os

'''
Main script for running indexer
'''
from .subcomponents.paper_loader import PaperLoader
from .subcomponents.paper_splitter import PaperSplitter
from .subcomponents.vectorstore import VectorIndexer

class PaperIndexer:
    def __init__(self):
        self.loader = PaperLoader()
        self.splitter = PaperSplitter()
        self.vector_indexer = VectorIndexer()

    def index_paper(self, pdf_path: str):
        print("Loading PDF...")
        documents = self.loader.load(pdf_path)

        print("Splitting text...")
        chunks = self.splitter.split(documents)

        print("Building vector index...")
        self.vector_indexer.build(chunks)

        print("Saving index at:")
        print(os.path.abspath(self.vector_indexer.index_path))
        self.vector_indexer.save()

        print("Indexing complete")