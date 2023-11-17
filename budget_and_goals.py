import json

# File name constants
BUDGET_FILE = 'budget.json'

def set_budget(category, amount):
    """Set budget for a specific category.

    Args:
    category (str): The category for the budget.
    amount (float): The budget amount.
    """
    try:
        with open(BUDGET_FILE, 'r+') as file:
            budget = json.load(file)
            budget[category] = amount
            file.seek(0)
            json.dump(budget, file, indent=4)
            file.truncate()
        print("Budget set successfully!")
    except FileNotFoundError:
        with open(BUDGET_FILE, 'w') as file:
            json.dump({category: amount}, file, indent=4)
        print("Budget file created and budget set successfully!")

# Testing code
if __name__ == "__main__":
    while True:
        choice = input("1. Set Budget\nChoose (1): ")  # Removed the option related to setting goals
        if choice == '1':
            category = input("Budget category: ")
            amount = float(input("Budget amount: "))
            set_budget(category, amount)
