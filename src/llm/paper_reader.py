from llm.prompt import PAPER_QA_PROMPT

class PaperReader:
    def __init__(self, retriever, llm):
        self.retriever = retriever
        self.llm = llm 

    def ask(self, question: str, k: int = 5):
        docs = self.retriever.retrieve(question, k)

        context = "\n\n".join(
            f"(Page {d.metadata.get('page')}) {d.page_content}"
            for d in docs
        )

        prompt = PAPER_QA_PROMPT.format(context=context, question=question)

        # llama_cpp call
        resp = self.llm(prompt)
        answer = resp['choices'][0]['text']

        return answer, docs

