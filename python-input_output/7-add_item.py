#!/usr/bin/python3
"""
Adds all command-line arguments to a Python list and saves them
as a JSON representation in a file named add_item.json.
"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """
    Loads a list from add_item.json, adds command-line arguments to it,
    and saves the updated list back to the file.
    """
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")


if __name__ == "__main__":
    main()

