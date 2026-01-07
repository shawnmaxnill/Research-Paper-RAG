import os
from indexer.paper_indexer import PaperIndexer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # paper_exp/src
PROJECT_ROOT = os.path.dirname(BASE_DIR)                # paper_exp
PDF_DIR = os.path.join(PROJECT_ROOT, "data", "papers")

def find_single_pdf(folder: str) -> str:
    pdfs = [f for f in os.listdir(folder) if f.lower().endswith(".pdf")]

    if len(pdfs) == 0:
        raise FileNotFoundError(f"No PDF found in {folder}")

    if len(pdfs) > 1:
        raise RuntimeError(f"Expected 1 PDF, found {len(pdfs)}: {pdfs}")

    return os.path.join(folder, pdfs[0])

def main():

    pdf_path = find_single_pdf(PDF_DIR)
    print(f"Found PDF: {pdf_path}")

    indexer = PaperIndexer()
    indexer.index_paper(pdf_path)  # change path

if __name__ == "__main__":
    main()
