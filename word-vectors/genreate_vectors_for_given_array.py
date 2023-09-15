from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity
import json


array = ['novel', 'bytes', 'quiz', 'audiobook', 'podcast', 'news', 'book', 'summary', 'course', 'story',
 'fitness', 'fantasy',  'science', 'information', 'horror', 'thriller', 'religion', 'motivation', 'how'
 'comedy', 'love', 'historical', 'career', 'crime', 'entertainment', 'finance', 'business', 'poems', 'shayari']

not_valid_words = ['how to', 'sci fi', 'poems shayari', 'personal finance', 'self help', 'book summary']


word_vectors = KeyedVectors.load_word2vec_format('/content/file.bin.gz', binary=True)
data = []
for word in array:
    vectors = word_vectors.get(word)
    data.append((word, word_vectors))


with open("/home/ubuntu/kukufm-py/kukufm-py/word-set.json", "w") as outfile:
    json.dump(word_set, outfile)