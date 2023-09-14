"""
This Code is only compatible with kukufm code base
"""

from managers.google_translator_manager import GoogleTranslatorManager

def get_english_translation_of_text(text):
    google_translator_manager = GoogleTranslatorManager()
    english_translated_title = google_translator_manager.translate(text)
    return english_translated_title


from channels.models import *


shows = Channel.objects.filter(language_id=1, status='live', is_premium=True, is_kuku_exclusive=True)

data = []
for show in shows:
    title = get_english_translation_of_text(show.title)
    desc = get_english_translation_of_text(show.description)
    doc = {'title': title, 'description' : desc}
    data.append(doc)

with open("shows.json", "w") as outfile:
    json.dump(data, outfile)