class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount):
        self.expenses.append((category, amount))

    def get_total_expenses(self):
        total = 0
        for _, amount in self.expenses:
            total += amount
        return total

    def get_expenses_by_category(self, category):
        category_expenses = self._filter_expenses_by_category(category)
        return [amount for _, amount in category_expenses]

    def get_categories(self):
        categories = set()
        for category, _ in self.expenses:
            categories.add(category)
        return categories

    def _filter_expenses_by_category(self, category):
        return [(cat, amount) for cat, amount in self.expenses if cat == category]


# Create an instance of ExpenseTracker
tracker = ExpenseTracker()

# Add some expenses
tracker.add_expense("Food", 50)
tracker.add_expense("Transportation", 30)
tracker.add_expense("Food", 20)
tracker.add_expense("Entertainment", 40)

# Get total expenses
total_expenses = tracker.get_total_expenses()
print("Total expenses:", total_expenses)

# Get expenses by category
food_expenses = tracker.get_expenses_by_category("Food")
print("Food expenses:", food_expenses)

# Get all categories
categories = tracker.get_categories()
print("Categories:", categories)