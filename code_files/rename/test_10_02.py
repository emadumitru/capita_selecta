import datetime
import unittest

# Import the functions from the original code
from pre_10_02 import calculate_total_expenses as pre_calculate_total_expenses
from pre_10_02 import display_expense_report as pre_display_expense_report

# Import the functions from the refactored code
from ref_10_02 import calculate_total_expenses as ref_calculate_total_expenses
from ref_10_02 import display_expense_report as ref_display_expense_report

class TestExpenseReport(unittest.TestCase):
    def setUp(self):
        # List to store expenses
        self.expenses = [
            {'date': datetime.date(2022, 1, 1), 'description': 'Groceries', 'amount': 50},
            {'date': datetime.date(2022, 1, 5), 'description': 'Dinner', 'amount': 30},
            {'date': datetime.date(2022, 1, 10), 'description': 'Movie tickets', 'amount': 20},
            {'date': datetime.date(2022, 1, 15), 'description': 'Gasoline', 'amount': 40},
            {'date': datetime.date(2022, 1, 20), 'description': 'Coffee', 'amount': 10}
        ]

    def test_pre_calculate_total_expenses(self):
        # Calculate total expenses using the original function
        pre_total_expenses = pre_calculate_total_expenses(self.expenses)

        # Calculate total expenses using the refactored function
        ref_total_expenses = ref_calculate_total_expenses(self.expenses)

        # Assert that the total expenses are the same
        self.assertEqual(pre_total_expenses, ref_total_expenses)

    def test_pre_display_expense_report(self):
        # Redirect stdout to capture the print output
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        # Display expense report using the original function
        pre_display_expense_report(self.expenses)

        # Get the captured print output
        pre_output = captured_output.getvalue()

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Redirect stdout again to capture the print output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Display expense report using the refactored function
        ref_display_expense_report(self.expenses)

        # Get the captured print output
        ref_output = captured_output.getvalue()

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Assert that the output is the same
        self.assertEqual(pre_output, ref_output)

if __name__ == '__main__':
    unittest.main()
