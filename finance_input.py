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

import pandas as pd

def delete_expense_record():
    try:
        df = pd.read_csv('expenses.csv')

        # Display current expense records with index
        print("Current Expense Records:")
        print(df.to_string(index=True))

        # Ask user for the index of the record to delete
        index_to_delete = int(input("Enter the index of the expense record to delete: "))

        # Check if index is valid
        if index_to_delete in df.index:
            # Delete the record
            df = df.drop(index_to_delete)

            # Save the updated DataFrame
            df.to_csv('expenses.csv', index=False)
            print("Expense record deleted successfully.")
        else:
            print("Invalid index entered.")
    except FileNotFoundError:
        print("Expenses file not found.")
    except ValueError:
        print("Invalid input, please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_income_record():
    try:
        df = pd.read_csv('income.csv')

        # Display current income records with index
        print("Current Income Records:")
        print(df.to_string(index=True))

        # Ask user for the index of the record to delete
        index_to_delete = int(input("Enter the index of the income record to delete: "))

        # Check if index is valid
        if index_to_delete in df.index:
            # Delete the record
            df = df.drop(index_to_delete)

            # Save the updated DataFrame
            df.to_csv('income.csv', index=False)
            print("Income record deleted successfully.")
        else:
            print("Invalid index entered.")
    except FileNotFoundError:
        print("Income file not found.")
    except ValueError:
        print("Invalid input, please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")








