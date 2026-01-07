# src/llm/llama_local.py
from llama_cpp import Llama

def load_llama(model_path="../../models/Meta-Llama-3-8B-Instruct.Q2_K.gguf"):
    """
    Returns a callable Llama instance
    """
    llm = Llama(model_path=model_path, n_ctx=2048, n_threads=8)
    return llm
