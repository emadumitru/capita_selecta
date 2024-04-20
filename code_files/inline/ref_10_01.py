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
        category_expenses = []
        for cat, amount in self.expenses:
            if cat == category:
                category_expenses.append(amount)
        return category_expenses

    def get_categories(self):
        categories = set()
        for category, _ in self.expenses:
            categories.add(category)
        return categories

    def track_expenses(self):
        # Add some expenses
        self.add_expense("Food", 50)
        self.add_expense("Transportation", 30)
        self.add_expense("Food", 20)
        self.add_expense("Entertainment", 40)

        # Get total expenses
        total_expenses = self.get_total_expenses()
        print("Total expenses:", total_expenses)

        # Get expenses by category
        food_expenses = self.get_expenses_by_category("Food")
        print("Food expenses:", food_expenses)

        # Get all categories
        categories = self.get_categories()
        print("Categories:", categories)


# Create an instance of ExpenseTracker
tracker = ExpenseTracker()

# Track expenses
tracker.track_expenses()