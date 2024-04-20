import unittest
from unittest.mock import patch
import pre_10_05
import ref_10_05

class TestExpenseTracker(unittest.TestCase):
    @patch('builtins.input', return_value="Food")
    @patch('builtins.print')
    def test_pre_expense_tracker(self, mock_print, mock_input):
        pre_10_05.expenses = [50, 30, 20, 10, 40]
        pre_10_05.total_expenses = pre_10_05.calculate_total_expenses(pre_10_05.expenses)
        pre_10_05.categorized_expenses = pre_10_05.categorize_expenses(pre_10_05.expenses)
        pre_10_05.display_expense_report(pre_10_05.total_expenses, pre_10_05.categorized_expenses)
        expected_calls = [
            unittest.mock.call('Expense Report'),
            unittest.mock.call('--------------'),
            unittest.mock.call('Total Expenses: $ 150'),
            unittest.mock.call('Categorized Expenses:'),
            unittest.mock.call('Food : $ 150'),
            unittest.mock.call('Transportation : $ 0'),
            unittest.mock.call('Entertainment : $ 0'),
            unittest.mock.call('Utilities : $ 0'),
            unittest.mock.call('Others : $ 0')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.input', return_value="Food")
    @patch('builtins.print')
    def test_ref_expense_tracker(self, mock_print, mock_input):
        ref_10_05.expenses = [50, 30, 20, 10, 40]
        ref_10_05.expense_tracker(ref_10_05.expenses)
        expected_calls = [
            unittest.mock.call('Expense Report'),
            unittest.mock.call('--------------'),
            unittest.mock.call('Total Expenses: $ 150'),
            unittest.mock.call('Categorized Expenses:'),
            unittest.mock.call('Food : $ 150'),
            unittest.mock.call('Transportation : $ 0'),
            unittest.mock.call('Entertainment : $ 0'),
            unittest.mock.call('Utilities : $ 0'),
            unittest.mock.call('Others : $ 0')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()