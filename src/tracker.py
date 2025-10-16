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
    return sum(exp["amount"] for exp in expenses if exp["category"].lower() == category.lower())

def edit_expense(index, new_description=None, new_category=None, new_amount=None):
    """Edita un gasto existente por índice."""
    expenses = load_data()
    if 0 <= index < len(expenses):
        if new_description:
            expenses[index]["description"] = new_description
        if new_category:
            expenses[index]["category"] = new_category
        if new_amount is not None:
            expenses[index]["amount"] = new_amount
        save_data(expenses)
        return expenses[index]
    else:
        raise IndexError("Índice fuera de rango.")

def delete_expense(index):
    """Elimina un gasto existente por índice."""
    expenses = load_data()
    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        save_data(expenses)
        return removed
    else:
        raise IndexError("Índice fuera de rango.")
