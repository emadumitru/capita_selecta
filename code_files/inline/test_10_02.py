import unittest
from unittest.mock import patch
import datetime
import pre_10_02
import ref_10_02

class TestExpenseTracker(unittest.TestCase):
    @patch('builtins.print')
    def test_pre_expense_tracker(self, mock_print):
        expenses = [
            {'date': datetime.date(2022, 1, 1), 'description': 'Groceries', 'amount': 50},
            {'date': datetime.date(2022, 1, 5), 'description': 'Dinner', 'amount': 30},
            {'date': datetime.date(2022, 1, 10), 'description': 'Movie tickets', 'amount': 20},
            {'date': datetime.date(2022, 1, 15), 'description': 'Gasoline', 'amount': 40},
            {'date': datetime.date(2022, 1, 20), 'description': 'Coffee', 'amount': 10}
        ]
        pre_10_02.display_expense_report(expenses)
        expected_calls = [
            unittest.mock.call('Expense Report:'),
            unittest.mock.call('----------------'),
            unittest.mock.call('2022-01-01: Groceries - $50'),
            unittest.mock.call('2022-01-05: Dinner - $30'),
            unittest.mock.call('2022-01-10: Movie tickets - $20'),
            unittest.mock.call('2022-01-15: Gasoline - $40'),
            unittest.mock.call('2022-01-20: Coffee - $10'),
            unittest.mock.call('----------------'),
            unittest.mock.call('Total Expenses: $150')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.print')
    def test_ref_expense_tracker(self, mock_print):
        expenses = [
            {'date': datetime.date(2022, 1, 1), 'description': 'Groceries', 'amount': 50},
            {'date': datetime.date(2022, 1, 5), 'description': 'Dinner', 'amount': 30},
            {'date': datetime.date(2022, 1, 10), 'description': 'Movie tickets', 'amount': 20},
            {'date': datetime.date(2022, 1, 15), 'description': 'Gasoline', 'amount': 40},
            {'date': datetime.date(2022, 1, 20), 'description': 'Coffee', 'amount': 10}
        ]
        ref_10_02.calculate_and_display_expense_report(expenses)
        expected_calls = [
            unittest.mock.call('Expense Report:'),
            unittest.mock.call('----------------'),
            unittest.mock.call('2022-01-01: Groceries - $50'),
            unittest.mock.call('2022-01-05: Dinner - $30'),
            unittest.mock.call('2022-01-10: Movie tickets - $20'),
            unittest.mock.call('2022-01-15: Gasoline - $40'),
            unittest.mock.call('2022-01-20: Coffee - $10'),
            unittest.mock.call('----------------'),
            unittest.mock.call('Total Expenses: $150')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()