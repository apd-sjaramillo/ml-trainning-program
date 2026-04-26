class MockAnswerService:
    def answer(self, question: str) -> str:
        return f"Mock answer: {question}"
