import csv
from datetime import datetime
from src.storage import load_data, save_data

def add_expense(description, category, amount, date=None):
    """Agrega un gasto con fecha (por defecto la fecha actual)."""
    expenses = load_data()
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    expense = {
        "description": description,
        "category": category,
        "amount": amount,
        "date": date
    }
    expenses.append(expense)
    save_data(expenses)
    return expense

def list_expenses():
    """Devuelve la lista completa de gastos."""
    return load_data()

def get_total_expense():
    """Suma el total de todos los gastos."""
    expenses = load_data()
    return sum(exp["amount"] for exp in expenses)

def get_expense_by_category(category):
    """Suma el total de gastos filtrados por categoría."""
    expenses = load_data()
    return sum(exp["amount"] for exp in expenses if exp["category"].lower() == category.lower())

def edit_expense(index, new_description=None, new_category=None, new_amount=None, new_date=None):
    """Edita un gasto existente por índice."""
    expenses = load_data()
    if 0 <= index < len(expenses):
        if new_description:
            expenses[index]["description"] = new_description
        if new_category:
            expenses[index]["category"] = new_category
        if new_amount is not None:
            expenses[index]["amount"] = new_amount
        if new_date:
            expenses[index]["date"] = new_date
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

def filter_by_date(date_str):
    """Filtra los gastos de una fecha específica (YYYY-MM-DD)."""
    expenses = load_data()
    return [exp for exp in expenses if exp["date"] == date_str]

def filter_by_month(month_str):
    """Filtra los gastos por mes (formato YYYY-MM)."""
    expenses = load_data()
    return [exp for exp in expenses if exp["date"].startswith(month_str)]

def export_to_csv(filename="gastos.csv"):
    """Exporta los gastos actuales a un archivo CSV."""
    expenses = load_data()
    if not expenses:
        raise ValueError("No hay gastos registrados para exportar.")
    
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["description", "category", "amount", "date"])
        writer.writeheader()
        writer.writerows(expenses)
    
    return filename
