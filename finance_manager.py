import pandas as pd
import json

# File path constants
EXPENSES_FILE = 'expenses.csv'
INCOME_FILE = 'income.csv'
BUDGET_FILE = 'budget.json'

def load_data(file_path):
    """Load financial data.

    Args:
    file_path (str): Path to the data file.

    Returns:
    DataFrame: A DataFrame containing financial data.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return pd.DataFrame()

def load_budget():
    """Load budget data."""
    try:
        with open(BUDGET_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Budget file not found.")
        return {}

def summarize_finances():
    """Summarize and analyze financial data."""
    expenses = load_data(EXPENSES_FILE)
    budget = load_budget()

    if not expenses.empty:
        total_expenses = expenses['amount'].sum()
        average_expense = expenses['amount'].mean()
        print(f"Total expenses: {total_expenses}, Average expense: {average_expense:.2f}")

        # Compare budget with actual expenses
        for category, amount in budget.items():
            category_expenses = expenses[expenses['category'] == category]['amount'].sum()
            status = 'Overspent' if category_expenses > amount else 'Within Budget'
            print(f"Category: {category}, Budget: {amount}, Actual: {category_expenses}, Status: {status}")
    else:
        print("No expense records found.")

    # Income part remains unchanged
    # ...

