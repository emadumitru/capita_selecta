import unittest
from unittest.mock import patch
import pre_10_03
import ref_10_03

class TestExpenseTracker(unittest.TestCase):
    @patch('builtins.input', side_effect=['Food', 'Transportation', 'Entertainment', 'Food', 'Transportation'])
    @patch('builtins.print')
    def test_pre_expense_tracker(self, mock_print, mock_input):
        expenses = [100, 50, 75, 120, 200]
        total_expenses = pre_10_03.calculate_total_expenses(expenses)
        expense_categories = pre_10_03.categorize_expenses(expenses)
        pre_10_03.display_expenses_by_category(expense_categories)
        expected_calls = [
            unittest.mock.call('Total expenses: 545'),
            unittest.mock.call('Food: [100, 120]'),
            unittest.mock.call('Transportation: [50, 200]'),
            unittest.mock.call('Entertainment: [75]')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.input', side_effect=['Food', 'Transportation', 'Entertainment', 'Food', 'Transportation'])
    @patch('builtins.print')
    def test_ref_expense_tracker(self, mock_print, mock_input):
        expenses = [100, 50, 75, 120, 200]
        total_expenses = ref_10_03.calculate_total_expenses(expenses)
        expense_categories = ref_10_03.categorize_expenses(expenses)
        ref_10_03.display_expenses_by_category(expense_categories)
        expected_calls = [
            unittest.mock.call('Total expenses: 545'),
            unittest.mock.call('Food: [100, 120]'),
            unittest.mock.call('Transportation: [50, 200]'),
            unittest.mock.call('Entertainment: [75]')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()