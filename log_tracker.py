

import json
from datetime import date

empty_json = {} 
empty_json_string = json.dumps(empty_json) 

LOG_FILE = "empty_json.json"


def load_log():
    try:
        with open(LOG_FILE, mode = "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_log(logs):
    with open(LOG_FILE, mode = "w") as file:
        json.dump(logs, file, indent = 4)


def add_food_to_log(logs, food, calories, category):
    date = input("Enter the date (YYYY-MM-DD): ").strip()

    if date not in logs:
        logs[date] = []

    logs[date].append({"food": food, "calories": calories, "category": category})
    print(f"Added {food.title()} ({category}) with {calories} calories to the log for {date}.")
    save_log(logs)


def view_daily_log(logs):
    date = input("Enter the date to view (YYYY-MM-DD): ").strip()
    if date not in logs:
        print(f"No entries for {date}")
        return

    print(f"Calories Log for {date}:")
    total = 0
    for entry in logs[date]:
        print(f"- {entry["food"].title()}: {entry["calories"]} calories")
        total += entry["calories"]

    print(f"Total: {total} calories")