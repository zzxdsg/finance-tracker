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


def delete_budget_category():
    try:
        with open('budget.json', 'r') as file:
            budget = json.load(file)

        # Convert budget to a list of tuples (for displaying with index)
        budget_list = list(budget.items())
        print("Current Budget Categories:")
        for idx, (category, amount) in enumerate(budget_list):
            print(f"{idx}: {category} - {amount}")

        # Ask user for the index of the category to delete
        index_to_delete = int(input("Enter the index of the budget category to delete: "))

        # Check if index is valid
        if 0 <= index_to_delete < len(budget_list):
            # Delete the category
            del budget[budget_list[index_to_delete][0]]

            with open('budget.json', 'w') as file:
                json.dump(budget, file, indent=4)
            print("Budget category deleted successfully.")
        else:
            print("Invalid index entered.")
    except FileNotFoundError:
        print("Budget file not found.")
    except ValueError:
        print("Invalid input, please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")


