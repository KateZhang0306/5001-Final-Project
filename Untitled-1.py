

import csv
from datetime import datetime

data = "nutrients.csv"

def load_data():
    entries = {}
    try:
        with open(data, mode = 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                entries[row["Food"].lower()] = {
                    'calories': int(row["Calories"]),
                    'category': row["Category"]
                }
    except FileNotFoundError:
        print("File not found. Starting with empty database.")

    return entries