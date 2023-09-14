import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer


import json


def load_json_file(filepath):
    with open(filepath, "r") as f:
        json_data = f.read()

    return json.loads(json_data)


documents = load_json_file("categories-with-vectors.json.json")
for doc in documents:
  doc[1] = np.array(doc[1])


target_title = 'history'
target_vector = word_vectors[target_title]

similarities = []
for doc in documents:
    similarity = cosine_similarity([target_vector], [doc[1]])[0][0]
    similarities.append((doc[0], similarity))

# Sort the documents by similarity (higher values are closer)
similarities.sort(key=lambda x: x[1], reverse=True)
