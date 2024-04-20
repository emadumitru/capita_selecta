import unittest
from pre_10_04 import calculate_total_expenses as pre_calculate_total_expenses, categorize_expenses as pre_categorize_expenses, display_expenses_by_category as pre_display_expenses_by_category
from ref_10_04 import calculate_total_expenses as ref_calculate_total_expenses, categorize_expenses as ref_categorize_expenses, display_expenses_by_category as ref_display_expenses_by_category
class TestExpenseTracker(unittest.TestCase):
    def test_calculate_total_expenses(self):
        expenses = [100, 50, 75, 120, 200]
        pre_total_expenses = pre_calculate_total_expenses(expenses)
        ref_total_expenses = ref_calculate_total_expenses(expenses)
        self.assertEqual(pre_total_expenses, ref_total_expenses)

    def test_categorize_expenses(self):
        expenses = [100, 50, 75, 120, 200]
        pre_categories = pre_categorize_expenses(expenses)
        ref_categories = ref_categorize_expenses(expenses)
        self.assertEqual(pre_categories, ref_categories)

    def test_display_expenses_by_category(self):
        categories = {'Food': [100, 50], 'Transportation': [75, 120], 'Shopping': [200]}
        pre_display_output = pre_display_expenses_by_category(categories)
        ref_display_output = ref_display_expenses_by_category(categories)
        self.assertEqual(pre_display_output, ref_display_output)

if __name__ == '__main__':
    unittest.main()
    
