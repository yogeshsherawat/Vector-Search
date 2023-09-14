import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def load_json_file(filepath):
    with open(filepath, "r") as f:
        json_data = f.read()

    return json.loads(json_data)


data = load_json_file("data-with-vectors.json")

for doc in data:
  doc['vectors'] = np.array(doc['vectors'])

documents = data


# Target title and vector for which you want to find closest neighbors
target_title = 'Only you ALICE'
target_vector = None  # Initialize to None

# Find the target vector
for doc in documents:
    if doc['title'] == target_title:
        target_vector = doc['vector']
        break

print(doc)

if target_vector is None:
    print(f"Target title '{target_title}' not found.")
else:
    # Calculate cosine similarity between the target vector and all other vectors
    similarities = []
    for doc in documents:
        if doc['title'] != target_title:
            similarity = cosine_similarity([target_vector], [doc['vectors']])[0][0]
            similarities.append((doc['title'], doc['description'], similarity))

    # Sort the documents by similarity (higher values are closer)
    similarities.sort(key=lambda x: x[2], reverse=True)

    # Number of closest neighbors to retrieve
    K = 5  # Change to your desired value

    # Get the top K closest neighbors
    closest_neighbors = similarities[:K]

    # Print the closest neighbors
    print(f"Top {K} closest neighbors to '{target_title}':")
    for neighbor in closest_neighbors:
        print(f"Title: {neighbor[0]}, Description: {neighbor[1]}, Similarity: {neighbor[2]}")

