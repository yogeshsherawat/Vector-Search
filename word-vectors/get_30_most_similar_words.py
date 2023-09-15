

def get_similar_words(category, vector, word_vectors, K=30):
    similarities = []
    for word in word_vectors:
        similarity = cosine_similarity([vector], [word_vectors[word]])[0][0]
        similarities.append((word, similarity))
    similarities.sort(key=lambda x: x[1], reverse=True)
    closest_neighbors = similarities[:K]
    closest_words = [i[0] for i in closest_neighbors]
    return closest_words


