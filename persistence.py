import json
import os

DB_FILE = "notifylib_db.json"

def save_event(event_name, data):
    db = {}
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            db = json.load(f)
    db[event_name] = data
    with open(DB_FILE, "w") as f:
        json.dump(db, f)

def load_event(event_name):
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            db = json.load(f)
        return db.get(event_name, None)
    return None
