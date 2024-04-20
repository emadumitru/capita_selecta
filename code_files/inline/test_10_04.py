import unittest
from unittest.mock import patch
import pre_10_04
import ref_10_04

class TestExpenseTracker(unittest.TestCase):
    @patch('builtins.input', return_value="Food")
    @patch('builtins.print')
    def test_pre_expense_tracker(self, mock_print, mock_input):
        pre_10_04.main()
        expected_calls = [
            unittest.mock.call('Total Expenses: 545'),
            unittest.mock.call(),
            unittest.mock.call('Category: Food'),
            unittest.mock.call('Expenses: [100, 50, 75, 120, 200]'),
            unittest.mock.call()
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.input', return_value="Food")
    @patch('builtins.print')
    def test_ref_expense_tracker(self, mock_print, mock_input):
        ref_10_04.main()
        expected_calls = [
            unittest.mock.call('Total Expenses: 545'),
            unittest.mock.call(),
            unittest.mock.call('Category: Food'),
            unittest.mock.call('Expenses: [100, 50, 75, 120, 200]'),
            unittest.mock.call()
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()