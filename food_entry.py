

import csv
from datetime import datetime

data = "nutrients.csv"

def load_data():
    entries = {}
    try:
        with open(data, mode = 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    entries[row["Food"].lower()] = {
                        'calories': int(row["Calories"].replace(",", "")),
                        'category': row["Category"]
                    }
                except:
                    print()
    except FileNotFoundError:
        print("File not found. Starting with empty database.")

    return entries


def add_food(entries):
    food = input("Enter the food name: ").strip().lower()
    if food in entries:
        print(f"{food.title()} is in database")
        return
    
    try:
        calories = int(input("Enter the calories of the food: "))
        category = input("Enter the category of the food: ")
    except ValueError:
        print("Invalid value. Please enter integer for calories.")
        return

    entries[food] = {'calories': calories, 'category': category}
    print(f"{food.title()} added to the food database with {calories} calories in the {category} category.")
    


def search_food(entries):
    food = input("Enter the food you want to search: ").strip().lower()

    if food in entries:
        details = entries[food]
        print(f"{food.title()} has {details['calories']} calories. Category: {details['category']}.")

        update_ask = input("Do you want to update the calories? (yes/no)").strip().lower()

        if update_ask == 'yes':
            new_cal = int(input("Enter the new calories: "))
            entries[food]['calories'] = new_cal
            print(f"{food.title()} updated to {new_cal} calories.")
    
    else:
        print(f"{food.title()} is not in the database.")