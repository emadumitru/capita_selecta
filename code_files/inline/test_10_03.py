import unittest
from unittest.mock import patch
import pre_10_03
import ref_10_03

class TestExpenseTracker(unittest.TestCase):
    @patch('builtins.input', return_value="Food")
    @patch('builtins.print')
    def test_pre_expense_tracker(self, mock_print, mock_input):
        pre_10_03.expenses = [100, 50, 75, 120, 200]
        pre_10_03.total_expenses = pre_10_03.calculate_total_expenses(pre_10_03.expenses)
        pre_10_03.expense_categories = pre_10_03.categorize_expenses(pre_10_03.expenses)
        pre_10_03.display_expenses_by_category(pre_10_03.expense_categories)
        expected_calls = [
            unittest.mock.call('Total expenses: 545'),
            unittest.mock.call('Food: [100, 50, 75, 120, 200]')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.input', return_value="Food")
    @patch('builtins.print')
    def test_ref_expense_tracker(self, mock_print, mock_input):
        ref_10_03.track_expenses()
        expected_calls = [
            unittest.mock.call('Total expenses: 545'),
            unittest.mock.call('Food: [100, 50, 75, 120, 200]')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()