

from food_entry import load_data, search_food, add_food
from log_tracker import load_log, add_food_to_log, view_daily_log

def main():
    food_database = load_data()
    logs = load_log()

    while True:
        print("\nWelcome to the Calorie Tracker")
        print("1. Search for food in database")
        print("2. Add food to log")
        print("3. Print log for a date")
        print("4. Add food to the database")
        print("5. Exit")

        choice = input("Enter your option: ").strip()

        if choice == "1":
            search_food(food_database)

        elif choice == "2":
            food = input("Enter the food name: ").strip().lower()
            if food in food_database:
                calories = food_database[food]["calories"]
                category = food_database[food]["category"]
            else:
                print(f"{food.title()} is not in the database.")
                add = input("Would you like to add it? (yes/no): ").strip().lower()
                if add == "yes":
                    add_food(food_database)
                    continue
                else:
                    print("Okay then.")
                    continue
            add_food_to_log(logs, food, calories, category)

        elif choice == "3":
            view_daily_log(logs)

        elif choice == "4":
            add_food(food_database)

        elif choice == "5":
            print("Thank you and goodbye!")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()