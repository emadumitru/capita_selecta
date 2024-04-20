import datetime

# Function to calculate total expenses and display expense report
def calculate_and_display_expense_report(expenses):
    total = 0
    print("Expense Report:")
    print("----------------")
    for expense in expenses:
        total += expense['amount']
        print(f"{expense['date']}: {expense['description']} - ${expense['amount']}")
    print("----------------")
    print(f"Total Expenses: ${total}")

# List to store expenses
expenses = [
    {'date': datetime.date(2022, 1, 1), 'description': 'Groceries', 'amount': 50},
    {'date': datetime.date(2022, 1, 5), 'description': 'Dinner', 'amount': 30},
    {'date': datetime.date(2022, 1, 10), 'description': 'Movie tickets', 'amount': 20},
    {'date': datetime.date(2022, 1, 15), 'description': 'Gasoline', 'amount': 40},
    {'date': datetime.date(2022, 1, 20), 'description': 'Coffee', 'amount': 10}
]

# Call the function to calculate and display the expense report
calculate_and_display_expense_report(expenses)
