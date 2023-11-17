import auth
import finance_input
import finance_manager
import budget_and_goals
import finance_visualization
import finance_report
import logging

# Initialize logging
logging.basicConfig(filename='app.log', level=logging.INFO)

def main_menu():
    """Display the main menu and get the user's choice"""
    print("\nWelcome to the Personal Finance Tracker")
    print("1. Log In")
    print("2. Register")
    print("3. Record Expense")
    print("4. Record Income")
    print("5. Generate Financial Report")
    print("6. View Financial Charts")
    print("7. Set Budget")
    print("8. Financial Management")
    print("9. Exit")
    return input("Please choose an option: ")

def main():
    is_logged_in = False  # Track whether the user is logged in

    while True:
        choice = main_menu()

        try:
            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                success, message = auth.login(username, password)
                print(message)
                if success:
                    is_logged_in = True  # Update the login status to True
            elif choice == '2':
                username = input("Enter username: ").strip()
                password = input("Enter password: ").strip()
                contact = input("Enter contact information: ").strip()
                if not username or not password:
                    print("Username and password cannot be empty.")
                else:
                    success, message = auth.register(username, password, contact)
                    print(message)
            elif is_logged_in:  # The following functions require login to access
                if choice == '3':
                    finance_input.record_expense()
                elif choice == '4':
                    finance_input.record_income()
                elif choice == '5':
                    finance_report.generate_report()
                elif choice == '6':
                    finance_visualization.plot_expenses()
                    finance_visualization.plot_income()
                elif choice == '7':
                    category = input("Budget category: ")
                    amount = float(input("Budget amount: "))
                    budget_and_goals.set_budget(category, amount)
                elif choice == '8':
                    finance_manager.summarize_finances()
            elif choice == '9':
                break
            else:
                print("Invalid option, please re-enter.")
        except Exception as e:
            logging.error(f"An error occurred: {e}", exc_info=True)
            print(f"An error occurred: {e}. Please check the log file for more information.")

if __name__ == "__main__":
    main()
