import csv
import os
from datetime import datetime


expenses = []
monthly_budget = 0.0
expense_file = "expenses.csv"


def load_expenses():
    global expenses
    if os.path.exists(expense_file):
        with open(expense_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    row['amount'] = float(row['amount'].strip())
                    row['date'] = row['date'].strip()
                    row['category'] = row['category'].strip()
                    row['description'] = row['description'].strip()
                    expenses.append(row)
                except Exception as e:
                    print(f"Skipping row due to error: {e}")
        print(f"Loaded {len(expenses)} expenses from file.")
        i = 1
        for exp in expenses:
         print(f"{i}. {exp}")
         i += 1

    else:
        print("No saved expenses found.")


def save_expenses():
    with open(expense_file, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['date', 'category', 'amount', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for exp in expenses:
            writer.writerow(exp)
    print("Expenses saved successfully!")


def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format!")
        return

    category = input("Enter category (e.g., Food, Travel): ").strip()
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Amount must be a number!")
        return

    description = input("Enter description: ").strip()

    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }
    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n📄 All Expenses:")
    print("-" * 60)
    for i, exp in enumerate(expenses, 1):
        if all(k in exp for k in ['date', 'category', 'amount', 'description']):
            print(f"{i}. {exp['date']} | {exp['category']} | ₹{exp['amount']:.2f} | {exp['description']}")
        else:
            print(f"{i}. Incomplete entry skipped.")
    print("-" * 60)


def set_budget():
    global monthly_budget
    try:
        monthly_budget = float(input("Enter your monthly budget: "))
        print(f"Budget of ₹{monthly_budget:.2f} set successfully!")
    except ValueError:
        print("Invalid input! Budget must be a number.")


def track_budget():
    if monthly_budget == 0:
        print("No budget set yet. Please set it first.")
        return

    total_spent = sum(exp['amount'] for exp in expenses)
    print(f"\nTotal spent so far: ₹{total_spent:.2f}")
    if total_spent > monthly_budget:
        print("You have exceeded your budget!")
    else:
        remaining = monthly_budget - total_spent
        print(f" You have ₹{remaining:.2f} left for the month.")

def show_menu():
    while True:
        print("\n========= Personal Expense Tracker =========")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Track budget")
        print("4. Save expenses")
        print("5. Set budget")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            track_budget()
        elif choice == '4':
            save_expenses()
        elif choice == '5':
            set_budget()
        elif choice == '6':
            save_expenses()
            print("Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice! Please enter a number between 1 and 6.")


load_expenses()
show_menu()
