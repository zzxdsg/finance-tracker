import auth
import finance_input
import finance_manager
import budget_and_goals
import finance_visualization
import finance_report
import logging

# Initialize logging
logging.basicConfig(filename='app.log', level=logging.INFO)

def display_user_manual():
    """Display the user manual for the software."""
    print("\nWelcome to the Personal Finance Tracker\n")
    print("This financial management software is designed to help you manage your income, expenses, and budget effectively. Here is a basic guide to using the software:")
    print("\n1. Registration and Login:")
    print("   - Register with a username and password upon first use.")
    print("   - Log in with these credentials each time you use the software.")
    print("\n2. Record Income and Expenses:")
    print("   - After logging in, start recording your income and expenses.")
    print("   - For each record, enter the relevant amount, category, and description.")
    print("\n3. View Financial Reports and Charts:")
    print("   - Generate and view financial reports to understand your total expenses, income, and savings.")
    print("   - View financial charts for a visual representation of your financial distribution.")
    print("\n4. Set Budgets:")
    print("   - Use the budget feature to set budget limits for different categories.")
    print("   - Enter the budget amount and the corresponding category.")
    print("\n5. Delete Records:")
    print("   - If necessary, previously recorded income, expenses, or budget items can be deleted.")
    print("   - Simply enter the index number of the item to delete it.")
    print("\nPlease use the delete function cautiously as deleted information cannot be recovered.")
    print("\nSummary: This software provides a comprehensive financial management solution, catering to your needs from simple record-keeping to complex analysis and budget management. Utilize this software to better understand and plan your financial status.")


def display_user_manual_cn():
    """展示软件的用户手册（中文版）。"""
    print("\n欢迎使用个人财务追踪器\n")
    print("这款财务管理软件旨在帮助您有效管理您的收入、支出和预算。以下是软件的基本使用指南：")
    print("\n1. 注册和登录：")
    print("   - 首次使用时需要注册，创建一个用户名和密码。")
    print("   - 每次使用软件时都需使用这些凭证登录。")
    print("\n2. 记录收入和支出：")
    print("   - 登录后，开始记录您的收入和支出。")
    print("   - 每一笔记录，请输入相关的金额、分类和描述。")
    print("\n3. 查看财务报告和图表：")
    print("   - 生成并查看财务报告，了解您的总支出、收入和储蓄。")
    print("   - 查看财务图表，直观展示您的财务分布。")
    print("\n4. 设定预算：")
    print("   - 使用预算功能为不同类别设定预算限额。")
    print("   - 输入预算金额及对应的类别。")
    print("\n5. 删除记录：")
    print("   - 如有必要，可以删除之前记录的收入、支出或预算条目。")
    print("   - 只需输入条目的索引号即可删除。")
    print("\n请谨慎使用删除功能，因为删除后的信息无法恢复。")
    print("\n总结：这款软件提供全面的财务管理解决方案，满足您从简单的记录保存到复杂的分析和预算管理的需求。利用这款软件，更好地理解和规划您的财务状况。")

def main_menu():
    """Display the main menu and get the user's choice"""
    print("\nWelcome to the Personal Finance Tracker")
    print("0. User Manual")
    print("00. 用户手册")
    print("1. Log In")
    print("2. Register")
    print("3. Record Expense")
    print("4. Record Income")
    print("5. Generate Financial Report")
    print("6. View Financial Charts")
    print("7. Set Budget")
    print("8. Check Budget Status")
    print("9. Delete Expense Record")
    print("10. Delete Income Record")
    print("11. Delete Budget Category")
    return input("Please choose an option: ")

def main():
    is_logged_in = False  # Track whether the user is logged in

    while True:
        choice = main_menu()

        try:
            if choice == '0':
                display_user_manual()
            elif choice == '00':
                display_user_manual_cn()
            elif choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                success, message = auth.login(username, password)
                print(message)
                if success:
                    is_logged_in = True  # Update the login status to True
            elif choice == '2':
                username = input("Enter username: ").strip()
                password = input("Enter password: ").strip()
                if not username or not password:
                    print("Username and password cannot be empty.")
                else:
                    success, message = auth.register(username, password)
                    print(message)
            elif is_logged_in:  # Check if the user is logged in before accessing other features
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
                    finance_input.delete_expense_record()  # Function to delete an expense record
                elif choice == '10':
                    finance_input.delete_income_record()  # Function to delete an income record
                elif choice == '11':
                    budget_and_goals.delete_budget_category()  # Function to delete a budget category
            else:
                print("Please log in to access this feature.")
        except Exception as e:
            logging.error(f"An error occurred: {e}", exc_info=True)
            print(f"An error occurred: {e}. Please check the log file for more information.")

if __name__ == "__main__":
    main()

