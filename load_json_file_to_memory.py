import json


def load_json_file(filepath):
    with open(filepath, "r") as f:
        json_data = f.read()

    return json.loads(json_data)


data = load_json_file("data-with-vectors.json")
