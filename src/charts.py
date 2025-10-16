from collections import defaultdict
from src.storage import load_data

def _bar(value, max_value, width=40):
    if max_value <= 0:
        return ""
    length = int((value / max_value) * width)
    return "█" * max(length, 1)

def chart_by_category():
    expenses = load_data()
    if not expenses:
        print("No hay datos para graficar.")
        return
    totals = defaultdict(float)
    for e in expenses:
        totals[e["category"]] += e["amount"]
    max_val = max(totals.values())
    print("\n📊 Gastos por categoría:")
    for cat, val in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        print(f"{cat:15} {val:10.2f}  {_bar(val, max_val)}")

def chart_by_month():
    expenses = load_data()
    if not expenses:
        print("No hay datos para graficar.")
        return
    totals = defaultdict(float)
    for e in expenses:
        month = e["date"][:7]  # YYYY-MM
        totals[month] += e["amount"]
    max_val = max(totals.values())
    print("\n📆 Gastos por mes:")
    for month, val in sorted(totals.items()):
        print(f"{month:10} {val:10.2f}  {_bar(val, max_val)}")
