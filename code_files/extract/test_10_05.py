import unittest
from unittest.mock import patch
import pre_10_05
import ref_10_05

class TestExpenseTracker(unittest.TestCase):
    @patch('builtins.input', side_effect=['Food', 'Transportation', 'Entertainment', 'Utilities', 'Others'])
    @patch('builtins.print')
    def test_pre_expense_tracker(self, mock_print, mock_input):
        expenses = [50, 30, 20, 10, 40]
        total_expenses = pre_10_05.calculate_total_expenses(expenses)
        categorized_expenses = pre_10_05.categorize_expenses(expenses)
        pre_10_05.display_expense_report(total_expenses, categorized_expenses)
        expected_calls = [
            unittest.mock.call('Expense Report'),
            unittest.mock.call('--------------'),
            unittest.mock.call('Total Expenses: $ 150'),
            unittest.mock.call('Categorized Expenses:'),
            unittest.mock.call('Food : $ 50'),
            unittest.mock.call('Transportation : $ 30'),
            unittest.mock.call('Entertainment : $ 20'),
            unittest.mock.call('Utilities : $ 10'),
            unittest.mock.call('Others : $ 40')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.input', side_effect=['Food', 'Transportation', 'Entertainment', 'Utilities', 'Others'])
    @patch('builtins.print')
    def test_ref_expense_tracker(self, mock_print, mock_input):
        expenses = [50, 30, 20, 10, 40]
        total_expenses = ref_10_05.calculate_total_expenses(expenses)
        categorized_expenses = ref_10_05.categorize_expenses(expenses)
        ref_10_05.display_expense_report(total_expenses, categorized_expenses)
        expected_calls = [
            unittest.mock.call('Expense Report'),
            unittest.mock.call('--------------'),
            unittest.mock.call('Total Expenses: $ 150'),
            unittest.mock.call('Categorized Expenses:'),
            unittest.mock.call('Food : $ 50'),
            unittest.mock.call('Transportation : $ 30'),
            unittest.mock.call('Entertainment : $ 20'),
            unittest.mock.call('Utilities : $ 10'),
            unittest.mock.call('Others : $ 40')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()