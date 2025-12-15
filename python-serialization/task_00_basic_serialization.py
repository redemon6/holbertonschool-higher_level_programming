#!/usr/bin/python3
def serialize_and_save_to_file(data, filename):
    with open(filename, mode='wb', encoding="UTF-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    with open(filename, mode='rb', encoding="UTF-8") as f:
        return json.load(f)
