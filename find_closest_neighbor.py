import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Sample data: an array of documents with titles, descriptions, and vectors
documents = [
    {
        'title': 'Document 1',
        'description': 'This is the first document.',
        'vector': np.random.rand(384),  # Replace with your actual vector
    },
    {
        'title': 'Document 2',
        'description': 'This is the second document.',
        'vector': np.random.rand(384),  # Replace with your actual vector
    },
    {
        'title': 'Document 2',
        'description': 'This is the second document.',
        'vector': np.random.rand(384),  # Replace with your actual vector
    },
    {
        'title': 'Document 4',
        'description': 'This is the second document.',
        'vector': np.random.rand(384),  # Replace with your actual vector
    },
    # Add more documents here
]

# Target title and vector for which you want to find closest neighbors
target_title = 'Document 1'
target_vector = None  # Initialize to None

# Find the target vector
for doc in documents:
    if doc['title'] == target_title:
        target_vector = doc['vector']
        break

if target_vector is None:
    print(f"Target title '{target_title}' not found.")
else:
    # Calculate cosine similarity between the target vector and all other vectors
    similarities = []
    for doc in documents:
        if doc['title'] != target_title:
            similarity = cosine_similarity([target_vector], [doc['vector']])[0][0]
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
