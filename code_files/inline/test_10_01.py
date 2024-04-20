import unittest
from unittest.mock import patch
import pre_10_01
import ref_10_01

class TestExpenseTracker(unittest.TestCase):
    @patch('builtins.print')
    def test_pre_expense_tracker(self, mock_print):
        tracker = pre_10_01.ExpenseTracker()
        tracker.add_expense("Food", 50)
        tracker.add_expense("Transportation", 30)
        tracker.add_expense("Food", 20)
        tracker.add_expense("Entertainment", 40)
        total_expenses = tracker.get_total_expenses()
        food_expenses = tracker.get_expenses_by_category("Food")
        categories = tracker.get_categories()
        expected_calls = [
            unittest.mock.call('Total expenses:', 140),
            unittest.mock.call('Food expenses:', [50, 20]),
            unittest.mock.call('Categories:', {'Food', 'Transportation', 'Entertainment'})
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.print')
    def test_ref_expense_tracker(self, mock_print):
        tracker = ref_10_01.ExpenseTracker()
        tracker.track_expenses()
        expected_calls = [
            unittest.mock.call('Total expenses:', 140),
            unittest.mock.call('Food expenses:', [50, 20]),
            unittest.mock.call('Categories:', {'Food', 'Transportation', 'Entertainment'})
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()