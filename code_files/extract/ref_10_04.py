# Expense Tracker

# Function to calculate total expenses
def calculate_total_expenses(expenses):
    total = sum(expenses)
    return total

# Function to categorize expenses
def categorize_expenses(expenses):
    categories = {}
    for expense in expenses:
        category = input("Enter category for expense {}: ".format(expense))
        if category in categories:
            categories[category].append(expense)
        else:
            categories[category] = [expense]
    return categories

# Function to display expenses by category
def display_expenses_by_category(categories):
    for category, expenses in categories.items():
        print("Category: {}".format(category))
        print("Expenses: {}".format(expenses))
        print()

# Function to get expenses from user
def get_expenses():
    expenses = []
    num_expenses = int(input("Enter the number of expenses: "))
    for i in range(num_expenses):
        expense = float(input("Enter expense {}: ".format(i+1)))
        expenses.append(expense)
    return expenses

# Main function
def main():
    # Get expenses from user
    expenses = get_expenses()

    # Calculate total expenses
    total_expenses = calculate_total_expenses(expenses)
    print("Total Expenses: {}".format(total_expenses))
    print()

    # Categorize expenses
    categories = categorize_expenses(expenses)

    # Display expenses by category
    display_expenses_by_category(categories)

# Execute the main function
if __name__ == "__main__":
    main()