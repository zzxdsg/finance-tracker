import os
import pandas as pd

# Define file path constants
EXPENSES_FILE = 'expenses.csv'
INCOME_FILE = 'income.csv'

def generate_report():
    """Generate a comprehensive financial report"""
    # Check if files exist
    if not os.path.exists(EXPENSES_FILE) or not os.path.exists(INCOME_FILE):
        print("Please enter income and expense data first.")
        return

    try:
        expenses = pd.read_csv(EXPENSES_FILE)
        income = pd.read_csv(INCOME_FILE)

        total_expenses = expenses['amount'].sum()
        total_income = income['amount'].sum()
        savings = total_income - total_expenses

        print("Financial Report:")
        print(f"Total Expenses: {total_expenses}")
        print(f"Total Income: {total_income}")
        print(f"Savings: {savings}")

        # Further analysis can be added here
        # For example, analyzing expenses and income by month or category

    except FileNotFoundError as e:
        print(f"Data file missing: {e}")
    except Exception as e:
        print(f"Error occurred while generating report: {e}")

# Testing code
if __name__ == "__main__":
    generate_report()
