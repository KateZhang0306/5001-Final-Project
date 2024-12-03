

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


def add_food(entries):
    food = input("Enter the food name: ").strip().lower()
    if food in food_data:
        print(f"{food.title()} is in database")
        return
    
    try:
        calories = int(input("Enter the calories of the food: "))
        category = input("Enter the category of the food")
    except ValueError:
        print("Invalid value. Please enter integer for calories.")
        return

    entries[food] = {'calories': calories, 'category': category}
    print(f"{food.title()} added to the food database with {calories} calories in the {category} category.")
