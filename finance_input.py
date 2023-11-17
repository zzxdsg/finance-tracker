import csv
import pandas as pd
import os
import re

# File name constants
EXPENSES_FILE = 'expenses.csv'
INCOME_FILE = 'income.csv'

# Function to check if the input is in English
def is_english(input_str):
    return all(ord(c) < 128 for c in input_str)

def get_input(prompt, input_type=str):
    """Get user input and ensure it's in English."""
    while True:
        user_input = input(prompt)
        if input_type == float:
            try:
                return float(user_input)
            except ValueError:
                print("Please enter a valid number.")
                continue
        elif is_english(user_input):
            return user_input
        else:
            print("Only English input is accepted. Please try again.")

def record_expense():
    """Record an expense."""
    amount = get_input("Enter the expense amount: ", float)
    category = get_input("Enter the expense category: ")
    description = get_input("Enter the expense description: ")

    # Check if the file exists, if not, write the header row first
    if not os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["amount", "category", "description"])

    with open(EXPENSES_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, description])
    print("Expense recorded successfully!")

def record_income():
    """Record an income."""
    amount = get_input("Enter the income amount: ", float)
    source = get_input("Enter the income source: ")
    description = get_input("Enter the income description: ")

    # Check if the file exists, if not, write the header row first
    if not os.path.exists(INCOME_FILE):
        with open(INCOME_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["amount", "source", "description"])

    with open(INCOME_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([amount, source, description])
    print("Income recorded successfully!")

def import_data(file_path, data_type):
    """Import data from a CSV/Excel file."""
    if data_type not in ['expense', 'income']:
        print("Invalid data type!")
        return

    try:
        data = pd.read_csv(file_path)
        if data_type == 'expense':
            data.to_csv(EXPENSES_FILE, mode='a', header=False, index=False)
        else:
            data.to_csv(INCOME_FILE, mode='a', header=False, index=False)
        print("Data imported successfully!")
    except Exception as e:
        print(f"Error occurred while importing data: {e}")

# Testing code
if __name__ == "__main__":
    while True:
        choice = input("1. Record Expense\n2. Record Income\n3. Import Data\nPlease choose (1/2/3): ")
        if choice == '1':
            record_expense()
        elif choice == '2':
            record_income()
        elif choice == '3':
            file_path = get_input("Enter file path: ")
            data_type = get_input("Enter data type (expense/income): ")
            import_data(file_path, data_type)  # Data input and upload module
