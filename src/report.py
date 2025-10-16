from datetime import datetime, timedelta
from src.storage import load_data

def get_average_daily_expense():
    """Calcula el gasto promedio diario."""
    expenses = load_data()
    if not expenses:
        return 0
    dates = {exp["date"] for exp in expenses}
    total = sum(exp["amount"] for exp in expenses)
    return round(total / len(dates), 2)

def get_average_monthly_expense():
    """Calcula el gasto promedio mensual."""
    expenses = load_data()
    if not expenses:
        return 0
    months = {exp["date"][:7] for exp in expenses}
    total = sum(exp["amount"] for exp in expenses)
    return round(total / len(months), 2)

def get_most_expensive_category():
    """Devuelve la categoría con mayor gasto acumulado."""
    expenses = load_data()
    if not expenses:
        return None, 0
    totals = {}
    for e in expenses:
        cat = e["category"]
        totals[cat] = totals.get(cat, 0) + e["amount"]
    top_cat = max(totals, key=totals.get)
    return top_cat, totals[top_cat]

def get_days_without_expense():
    """Detecta días sin gasto entre la fecha mínima y máxima."""
    expenses = load_data()
    if not expenses:
        return []
    # Convertir fechas a objetos datetime
    dates = sorted({datetime.strptime(exp["date"], "%Y-%m-%d") for exp in expenses})
    start, end = dates[0], dates[-1]

    # Generar todas las fechas entre in
