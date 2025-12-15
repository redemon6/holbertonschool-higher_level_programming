#!/usr/bin/python3
import json, csv
def convert_csv_to_json(csv_file):
    try:
        # 1. Open and read the CSV file
        with open(csv_filename, 'r') as csvfile:
            # Use DictReader to treat each row as a dictionary where headers are keys
            csv_reader = list(csv.DictReader(csvfile))

    except FileNotFoundError:
        return False
    except Exception as e:
        return False
    

    try:
        with open('data.json', 'w') as jsonfile:
            # json.dump() serializes the list 'data' and writes it directly to the file
            json.dump(data, jsonfile, indent=4) 

        return True
    except Exception as e:
        return False
