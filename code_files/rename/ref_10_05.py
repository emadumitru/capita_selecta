# Expense Tracker

# Function to calculate total expenses
def calculate_total_expenses(expenses):
    total = sum(expenses)
    return total

# Function to categorize expenses
def categorize_expenses(expenses):
    categories = {
        'Food': 0,
        'Transportation': 0,
        'Entertainment': 0,
        'Utilities': 0,
        'Others': 0
    }

    for expense in expenses:
        category = input("Enter the category for expense: ")
        if category in categories:
            categories[category] += expense
        else:
            categories['Others'] += expense

    return categories

# Function to display expense report
def display_expense_report(total_expenses, categorized_expenses):
    print("Expense Report")
    print("--------------")
    print("Total Expenses: $", total_expenses)
    print("Categorized Expenses:")
    for category, expense in categorized_expenses.items():
        print(category, ": $", expense)

# Sample expenses
expenses = [50, 30, 20, 10, 40]

# Calculate total expenses
total_expenses = calculate_total_expenses(expenses)

# Categorize expenses
categorized_expenses = categorize_expenses(expenses)

# Display expense report
display_expense_report(total_expenses, categorized_expenses)