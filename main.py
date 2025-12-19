import json
import os
from datetime import datetime

EXPENSES_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(EXPENSES_FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense(expenses):
    print("\n--- Add New Expense ---")
    
    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date_input:
        date_input = datetime.now().strftime("%Y-%m-%d")
    
    categories = ["Food", "Transport", "Entertainment", "Utilities", "Shopping", "Other"]
    print("\nCategories:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")
    
    cat_choice = input("Choose category (1-6): ").strip()
    try:
        category = categories[int(cat_choice) - 1]
    except (ValueError, IndexError):
        category = "Other"
    
    description = input("Enter description: ").strip()
    
    amount_input = input("Enter amount: ").strip()
    try:
        amount = float(amount_input)
    except ValueError:
        print("Invalid amount. Setting to 0.")
        amount = 0.0
    
    expense = {
        "date": date_input,
        "category": category,
        "description": description,
        "amount": amount
    }
    
    expenses.append(expense)
    save_expenses(expenses)
    print(f"\nExpense added: {category} - ${amount:.2f}")

def view_expenses(expenses):
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    total = 0
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. [{exp['date']}] {exp['category']}: {exp['description']} - ${exp['amount']:.2f}")
        total += exp['amount']
    
    print(f"\nTotal: ${total:.2f}")

def view_by_category(expenses):
    print("\n--- Expenses by Category ---")
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    categories = {}
    for exp in expenses:
        cat = exp['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(exp)
    
    for cat, cat_expenses in categories.items():
        cat_total = sum(e['amount'] for e in cat_expenses)
        print(f"\n{cat}: ${cat_total:.2f}")
        for exp in cat_expenses:
            print(f"  - [{exp['date']}] {exp['description']} - ${exp['amount']:.2f}")

def delete_expense(expenses):
    print("\n--- Delete Expense ---")
    if not expenses:
        print("No expenses to delete.")
        return
    
    view_expenses(expenses)
    choice = input("\nEnter expense number to delete (or 0 to cancel): ").strip()
    
    try:
        index = int(choice) - 1
        if 0 <= index < len(expenses):
            deleted = expenses.pop(index)
            save_expenses(expenses)
            print(f"Deleted: {deleted['category']} - ${deleted['amount']:.2f}")
        elif choice != "0":
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")

def main():
    print("=" * 40)
    print("   Expense Tracker")
    print("=" * 40)
    
    expenses = load_expenses()
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View by Category")
        print("4. Delete Expense")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ").strip()
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_by_category(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print("\nGoodbye! Keep tracking your expenses!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
