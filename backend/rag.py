from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class RAG:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.vectors = None
        self.texts = []

    def create_index(self, texts):
        self.texts = texts
        self.vectors = self.vectorizer.fit_transform(texts)

    def search(self, query, k=3):
        query_vec = self.vectorizer.transform([query])
        scores = (self.vectors @ query_vec.T).toarray().flatten()
        top_k = np.argsort(scores)[-k:][::-1]
        return [self.texts[i] for i in top_k]