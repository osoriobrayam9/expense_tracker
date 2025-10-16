from src.storage import load_data, save_data

def add_expense(description, category, amount):
    expenses = load_data()
    expense = {"description": description, "category": category, "amount": amount}
    expenses.append(expense)
    save_data(expenses)
    return expense

def list_expenses():
    return load_data()

def get_total_expense():
    expenses = load_data()
    return sum(exp["amount"] for exp in expenses)

def get_expense_by_category(category):
    expenses = load_data()
    return sum(exp["amount"] for exp in expenses if exp["category"] == category)
