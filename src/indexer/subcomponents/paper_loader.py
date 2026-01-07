'''
Loading in all PDF from data directory
'''

from langchain_community.document_loaders import PyPDFLoader

class PaperLoader:
    def load(self, pdf_path: str):
        loader = PyPDFLoader(pdf_path)
        return loader.load()
