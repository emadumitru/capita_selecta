import unittest
from pre_10_01 import ExpenseTracker as PreRefactoredExpenseTracker
from ref_10_01 import ExpenseTracker as RefactoredExpenseTracker
class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.pre_refactored_tracker = PreRefactoredExpenseTracker()
        self.refactored_tracker = RefactoredExpenseTracker()

        # Add some expenses to both trackers
        self.pre_refactored_tracker.add_expense("Food", 50)
        self.pre_refactored_tracker.add_expense("Transportation", 30)
        self.pre_refactored_tracker.add_expense("Food", 20)
        self.pre_refactored_tracker.add_expense("Entertainment", 40)

        self.refactored_tracker.add_expense("Food", 50)
        self.refactored_tracker.add_expense("Transportation", 30)
        self.refactored_tracker.add_expense("Food", 20)
        self.refactored_tracker.add_expense("Entertainment", 40)

    def test_get_total_expenses(self):
        pre_refactored_total_expenses = self.pre_refactored_tracker.get_total_expenses()
        refactored_total_expenses = self.refactored_tracker.get_total_expenses()
        self.assertEqual(pre_refactored_total_expenses, refactored_total_expenses)

    def test_get_expenses_by_category(self):
        pre_refactored_food_expenses = self.pre_refactored_tracker.get_expenses_by_category("Food")
        refactored_food_expenses = self.refactored_tracker.get_expenses_for_category("Food")
        self.assertEqual(pre_refactored_food_expenses, refactored_food_expenses)

    def test_get_categories(self):
        pre_refactored_categories = self.pre_refactored_tracker.get_categories()
        refactored_categories = self.refactored_tracker.get_categories()
        self.assertEqual(pre_refactored_categories, refactored_categories)

if __name__ == '__main__':
    unittest.main()
