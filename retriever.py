# retriever.py
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import os
import pickle

MODEL_NAME = "all-MiniLM-L6-v2"

class CodeRetriever:
    def __init__(self, index_path="faiss.index", meta_path="meta.pkl"):
        self.model = SentenceTransformer(MODEL_NAME)
        self.index_path = index_path
        self.meta_path = meta_path

        self.index = None
        self.meta = []

        if os.path.exists(index_path) and os.path.exists(meta_path):
            self.load()

    def load(self):
        self.index = faiss.read_index(self.index_path)
        with open(self.meta_path, "rb") as f:
            self.meta = pickle.load(f)

    def save(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.meta_path, "wb") as f:
            pickle.dump(self.meta, f)

    def build(self, docs):
        texts = [d["text"] for d in docs]
        embeds = self.model.encode(texts)
        embeds = np.array(embeds).astype('float32')

        self.index = faiss.IndexFlatL2(embeds.shape[1])
        self.index.add(embeds)

        self.meta = docs
        self.save()

    def retrieve(self, query, k=5):
        q_emb = self.model.encode([query]).astype('float32')
        D, I = self.index.search(q_emb, k)

        results = []
        for idx in I[0]:
            if idx < len(self.meta):
                results.append(self.meta[idx]["text"])
        return results
