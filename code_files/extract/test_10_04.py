import unittest
from unittest.mock import patch
import pre_10_04
import ref_10_04

class TestExpenseTracker(unittest.TestCase):
    @patch('builtins.input', side_effect=['Food', 'Transportation', 'Entertainment', 'Food', 'Transportation'])
    @patch('builtins.print')
    def test_pre_expense_tracker(self, mock_print, mock_input):
        expenses = [100, 50, 75, 120, 200]
        total_expenses = pre_10_04.calculate_total_expenses(expenses)
        expense_categories = pre_10_04.categorize_expenses(expenses)
        pre_10_04.display_expenses_by_category(expense_categories)
        expected_calls = [
            unittest.mock.call('Total Expenses: 545'),
            unittest.mock.call(),
            unittest.mock.call('Category: Food'),
            unittest.mock.call('Expenses: [100, 120]'),
            unittest.mock.call(),
            unittest.mock.call('Category: Transportation'),
            unittest.mock.call('Expenses: [50, 200]'),
            unittest.mock.call(),
            unittest.mock.call('Category: Entertainment'),
            unittest.mock.call('Expenses: [75]'),
            unittest.mock.call()
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.input', side_effect=['5', '100', '50', '75', '120', '200', 'Food', 'Transportation', 'Entertainment', 'Food', 'Transportation'])
    @patch('builtins.print')
    def test_ref_expense_tracker(self, mock_print, mock_input):
        expenses = ref_10_04.get_expenses()
        total_expenses = ref_10_04.calculate_total_expenses(expenses)
        expense_categories = ref_10_04.categorize_expenses(expenses)
        ref_10_04.display_expenses_by_category(expense_categories)
        expected_calls = [
            unittest.mock.call('Total Expenses: 545'),
            unittest.mock.call(),
            unittest.mock.call('Category: Food'),
            unittest.mock.call('Expenses: [100.0, 120.0]'),
            unittest.mock.call(),
            unittest.mock.call('Category: Transportation'),
            unittest.mock.call('Expenses: [50.0, 200.0]'),
            unittest.mock.call(),
            unittest.mock.call('Category: Entertainment'),
            unittest.mock.call('Expenses: [75.0]'),
            unittest.mock.call()
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()