
import unittest
import re
import sys
import os
from io import StringIO

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '/Users/katezhang/Documents/NEU/NEU/5001/5001-Final-Project')))

import food_entry, log_tracker

common_msg = lambda msg, expected, actual: f"{msg}\nExpected: {expected}\nActual: {actual}"

clean_spaces = lambda string: re.sub(r"\s+", "", string)

class TestCalorieTracker(unittest.TestCase):

    def test_search_and_update_food(self) -> None:
        '''Test search food to database function'''

        entries = {
                "apple": {"calories": 95, "category": "fruit"},
                "sandwich": {"calories": 250, "category": "meal"},
            }

        inputs = iter(["apple", "yes", "100"]) 
        def mock_input(prompt):
            return next(inputs)

        expected_entries = {
            "apple": {"calories": 100, "category": "fruit"}, 
            "sandwich": {"calories": 250, "category": "meal"},
        }

        original_input = __builtins__.input
        __builtins__.input = mock_input

        food_entry.search_food(entries) 

        self.assertEqual(entries, expected_entries)



    def test_add_food_to_log(self) -> None:
        '''Test add food to log function'''
        logs = {}
        food = "apple"
        calories = 95
        category = "fruit"
        date = "2024-12-03"


        expected_logs = {
            date: [{"food": food, "calories": calories, "category": category}]
        }

        inputs = iter(["2024-12-03"]) 
        def mock_input(prompt):
            return next(inputs)

        original_input = __builtins__.input
        __builtins__.input = mock_input

        log_tracker.add_food_to_log(logs, food, calories, category)

        self.assertEqual(logs, expected_logs)


    def test_add_food(self) -> None:
        """Test adding food to the database."""
        entries = {}

        inputs = iter(["apple", "95", "fruit"])
        expected_entries = {
            "apple": {"calories": 95, "category": "fruit"}
        }

        def mock_input(prompt):
            return next(inputs)

        original_input = __builtins__.input
        __builtins__.input = mock_input

        food_entry.add_food(entries)

        self.assertEqual(entries, expected_entries)


    def test_view_daily_log(self) -> None:
        """Test viewing a daily log."""
        logs = {
            "2024-12-03": [
                {"food": "apple", "calories": 95, "category": "fruit"},
                {"food": "sandwich", "calories": 250, "category": "meal"},
            ]
        }

        expected_output = (
            "Calories Log for 2024-12-03:\n"
            "- Apple: 95 calories\n"
            "- Sandwich: 250 calories\n"
            "Total: 345 calories\n"
        )

        inputs = iter(["2024-12-03"])
        def mock_input(prompt):
            return next(inputs)



        captured_output = StringIO()
        sys.stdout = captured_output
        __builtins__.input = mock_input

        log_tracker.view_daily_log(logs) 

        output = captured_output.getvalue()
        self.assertEqual(output, expected_output)



if __name__ == "__main__":
    unittest.main()
    