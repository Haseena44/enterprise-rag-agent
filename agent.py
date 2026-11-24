from rag import search_documents

class EnterpriseAgent:
    def __init__(self, db):
        self.db = db
        self.memory = []

    def run(self, question):
        context = search_documents(self.db, question)
        self.memory.append({"question": question, "context": context})
        answer = f"Question: {question}\n\nAnswer (From Documents):\n{context[:2000]}"
        return answer
