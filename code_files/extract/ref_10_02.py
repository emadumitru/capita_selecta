import datetime

# Function to calculate total expenses
def calculate_total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense['amount']
    return total

# Function to display expense report
def display_expense_report(expenses):
    print("Expense Report:")
    print("----------------")
    for expense in expenses:
        print(f"{expense['date']}: {expense['description']} - ${expense['amount']}")
    print("----------------")
    total_expenses = calculate_total_expenses(expenses)
    print(f"Total Expenses: ${total_expenses}")

# Function to extract specific functionality
def extract_specific_functionality(expenses):
    for expense in expenses:
        print(f"{expense['date']}: {expense['description']} - ${expense['amount']}")

# List to store expenses
expenses = [
    {'date': datetime.date(2022, 1, 1), 'description': 'Groceries', 'amount': 50},
    {'date': datetime.date(2022, 1, 5), 'description': 'Dinner', 'amount': 30},
    {'date': datetime.date(2022, 1, 10), 'description': 'Movie tickets', 'amount': 20},
    {'date': datetime.date(2022, 1, 15), 'description': 'Gasoline', 'amount': 40},
    {'date': datetime.date(2022, 1, 20), 'description': 'Coffee', 'amount': 10}
]

# Display expense report
display_expense_report(expenses)

# Extract specific functionality
extract_specific_functionality(expenses)