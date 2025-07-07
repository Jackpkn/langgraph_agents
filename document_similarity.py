from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np

load_dotenv()
embedding = OpenAIEmbeddings(model='', dimensions=300)
documents = [

]
query ='user-query'

doc_embeddings = embedding.embed_documents(documents)
query_embedding  = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(documents[index])
print("similarity score is: ", score)


class sum:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b
