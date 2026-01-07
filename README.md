### Research Paper Explainer using RAG + AI

This repo contains all code for running a paper explained by AI given a user input.
This was made at its simplest level with no UI, just running commands.

### Purpose
Demonstration of understanding

#### Steps to run:

1. Run `download_model.sh` to first download 'Meta-Llama-3-8B-Instruct.Q2_K' locally given that you created a HuggingFace account. This will also create a `models/llama3` nested file.
2. Run `file_manager.py` to insert your target research paper. Only one file can be read at a given time. This will create a `data/papers` nested file.
3. Run `run_indexer.py` to embed the target research paper. This will create a vector store which will be using by the LLM later on. 
   `run_indexer.py` uses subcomponents from `src/indexer/subcomponents`
   Models/Algo employed for this task:
   - Langchain Recursive Text Splitter
   - FAISS
   - Sentence Transformer: all-MiniLM-L6-v2
4. Run `main.py` which orchestrates everything together

Do keep in mind that this serves as a POC for future project as many improvements are planned to be done.

### File Contents
`src` contains main working directories: `indexer`, `retriever`, `llm`

`indexer`
Contains components used to build indexer: subcomponent directory, `paper_indexer.py` which puts all subcomponents together

`retriever`
Contains `vec_loader` and `vec_retriever` which are used for model RAG

`llm`
Contains components loading the LLM and what it output.
- Loads the model `load_local_model.py`
- Reads paper and answers with `paper_reader.py`
- `prompt.py` Main prompt for confining the LLM
- `citator.py` provides sources of where the information was found

