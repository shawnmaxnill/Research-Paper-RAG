from retriever.vec_loader import load_vectorstore
from retriever.vec_retriever import PaperRetriever
from llm.paper_reader import PaperReader
from llm.citator import format_sources
from llm.prompt import PAPER_QA_PROMPT
from llm.load_local_model import load_llama
import time


vectorstore = load_vectorstore("../data/vecstore")
retriever = PaperRetriever(vectorstore)

llm = load_llama("../models/llama3/Meta-Llama-3-8B-Instruct.Q2_K.gguf")

reader = PaperReader(retriever, llm)

question = input("Ask a question: ")

start_time = time.perf_counter()

answer, docs = reader.ask(question)

end_time = time.perf_counter()

print("\nANSWER:\n", answer)
print("\n" + format_sources(docs))
print("\nTime taken: {:.4f} seconds".format(end_time - start_time))