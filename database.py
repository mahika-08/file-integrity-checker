import json
import os


def load_hashes():
    if not os.path.exists("database.json"):
        return {}

    with open("database.json", "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}


def save_hashes(hash_data):
    with open("database.json", "w") as file:
        json.dump(hash_data, file, indent=4)