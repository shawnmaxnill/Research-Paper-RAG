mkdir -p models/llama3

huggingface-cli download \
  MaziyarPanahi/Meta-Llama-3-8B-Instruct-GGUF \
  --local-dir models/llama3 \
  --include "*Q2_K*.gguf"
