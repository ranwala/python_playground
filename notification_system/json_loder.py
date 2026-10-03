import json

def load_json(cls, file_path):
    with open(file_path, 'r') as file:
        return [cls(**d) for d in json.load(file)]


def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump([vars(item) for item in data], file, indent=4)