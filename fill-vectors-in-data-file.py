import json
from sentence_transformers import SentenceTransformer

data = json.load(open('/content/data.json'))
model = SentenceTransformer('all-MiniLM-L6-v2')

for show in data:
    print(show["title"])
    sentences = [f'{show["title"]}. {show["description"]}']
    sentence_embeddings = model.encode(sentences)
    show['vectors'] = sentence_embeddings[0].tolist()

with open("/content/data-with-vectors.json", "w") as outfile:
    json.dump(data, outfile)