import json
from channels.models import Channel

shows = Channel.objects.filter(language_id=1, status='live', is_premium=True, is_kuku_exclusive=True)

data = []
for show in shows:
    doc = {'id':show.id, 'title': show.title, 'description' : show.description}
    data.append(doc)

with open("shows.json", "w") as outfile:
    json.dump(data, outfile)