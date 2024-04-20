import unittest
from unittest.mock import patch
import pre_10_01
import ref_10_01

class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.categories = ["Food", "Transportation", "Entertainment"]
        self.amounts = [50, 30, 20, 40]
        self.expenses = list(zip(self.categories, self.amounts))

    def test_pre_expense_tracker(self):
        tracker = pre_10_01.ExpenseTracker()
        for category, amount in self.expenses:
            tracker.add_expense(category, amount)
        self.assertEqual(tracker.get_total_expenses(), sum(self.amounts))
        self.assertEqual(tracker.get_expenses_by_category("Food"), [50, 20])
        self.assertEqual(tracker.get_categories(), set(self.categories))

    def test_ref_expense_tracker(self):
        tracker = ref_10_01.ExpenseTracker()
        for category, amount in self.expenses:
            tracker.add_expense(category, amount)
        self.assertEqual(tracker.get_total_expenses(), sum(self.amounts))
        self.assertEqual(tracker.get_expenses_by_category("Food"), [50, 20])
        self.assertEqual(tracker.get_categories(), set(self.categories))

if __name__ == '__main__':
    unittest.main()