import unittest
from pre_10_05 import calculate_total_expenses as pre_calculate_total_expenses, categorize_expenses as pre_categorize_expenses, display_expense_report as pre_display_expense_report
from ref_10_05 import calculate_total_expenses as ref_calculate_total_expenses, categorize_expenses as ref_categorize_expenses, display_expense_report as ref_display_expense_report
class TestExpenseTracker(unittest.TestCase):
    def test_calculate_total_expenses(self):
        expenses = [50, 30, 20, 10, 40]
        pre_total_expenses = pre_calculate_total_expenses(expenses)
        ref_total_expenses = ref_calculate_total_expenses(expenses)
        self.assertEqual(pre_total_expenses, ref_total_expenses)

    def test_categorize_expenses(self):
        expenses = [50, 30, 20, 10, 40]
        pre_categorized_expenses = pre_categorize_expenses(expenses)
        ref_categorized_expenses = ref_categorize_expenses(expenses)
        self.assertEqual(pre_categorized_expenses, ref_categorized_expenses)

    def test_display_expense_report(self):
        expenses = [50, 30, 20, 10, 40]
        pre_total_expenses = pre_calculate_total_expenses(expenses)
        pre_categorized_expenses = pre_categorize_expenses(expenses)
        ref_total_expenses = ref_calculate_total_expenses(expenses)
        ref_categorized_expenses = ref_categorize_expenses(expenses)

        pre_report = pre_display_expense_report(pre_total_expenses, pre_categorized_expenses)
        ref_report = ref_display_expense_report(ref_total_expenses, ref_categorized_expenses)

        self.assertEqual(pre_report, ref_report)

if __name__ == '__main__':
    unittest.main()