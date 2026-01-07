
class PaperRetriever:
    def __init__(self, vectorstore):
        self.vectorstore = vectorstore

    def retrieve(self, query, k: int = 5):
        return self.vectorstore.similarity_search(query, k=k)


# Converts user input (query) into embeddings
# do KNN
# It just searches sets of words that might be the answer.