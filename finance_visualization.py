import matplotlib.pyplot as plt
import pandas as pd
import chardet

# File path constants
EXPENSES_FILE = 'expenses.csv'
INCOME_FILE = 'income.csv'

# Function to detect file encoding
def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        return chardet.detect(file.read(100000))['encoding']

def plot_expenses():
    """Generate a pie chart of expenses"""
    try:
        expenses_encoding = detect_encoding(EXPENSES_FILE)
        expenses = pd.read_csv(EXPENSES_FILE, encoding=expenses_encoding)
        if 'amount' not in expenses.columns or 'category' not in expenses.columns:
            print("Expenses data file is incorrectly formatted, missing necessary columns.")
            return
        if expenses.empty:
            print("No expense data to display.")
            return

        summary = expenses.groupby('category')['amount'].sum()
        summary.plot(kind='pie', autopct='%1.1f%%')
        plt.title('Expense Distribution')
        plt.ylabel('')
        plt.show()
    except FileNotFoundError:
        print("Expenses data file not found.")
    except Exception as e:
        print(f"Error generating chart: {e}")

def plot_income():
    """Generate a bar chart of income"""
    try:
        income_encoding = detect_encoding(INCOME_FILE)
        income = pd.read_csv(INCOME_FILE, encoding=income_encoding)
        if 'amount' not in income.columns or 'source' not in income.columns:
            print("Income data file is incorrectly formatted, missing necessary columns.")
            return
        if income.empty:
            print("No income data to display.")
            return

        summary = income.groupby('source')['amount'].sum()
        summary.plot(kind='bar')
        plt.title('Income Sources')
        plt.xlabel('Source')
        plt.ylabel('Amount')
        plt.show()
    except FileNotFoundError:
        print("Income data file not found.")
    except Exception as e:
        print(f"Error generating chart: {e}")

# Testing code
if __name__ == "__main__":
    choice = input("1. Display Expense Chart\n2. Display Income Chart\nChoose (1/2): ")
    if choice == '1':
        plot_expenses()
    elif choice == '2':
        plot_income()
