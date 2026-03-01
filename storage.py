# storage.py - save and load data from a JSON file

import json, os
from models import User

FILE = os.path.join(os.path.dirname(__file__), "data", "store.json")

def load():
    try:
        with open(FILE) as f:
            return [User.from_dict(u) for u in json.load(f)["users"]]
    except (FileNotFoundError, KeyError):
        return []

def save(users):
    os.makedirs(os.path.dirname(FILE), exist_ok=True)
    with open(FILE, "w") as f:
        json.dump({"users": [u.to_dict() for u in users]}, f, indent=2)
