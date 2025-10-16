import json
from datetime import datetime
from pathlib import Path
from src.storage import load_data

BUDGET_FILE = Path("budget.json")

def set_monthly_budget(amount):
    """Establece un presupuesto mensual general."""
    data = {"budget": amount, "last_updated": datetime.now().strftime("%Y-%m-%d")}
    with open(BUDGET_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    return data

def get_monthly_budget():
    """Obtiene el presupuesto mensual actual."""
    if BUDGET_FILE.exists():
        with open(BUDGET_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"budget": 0, "last_updated": None}

def get_monthly_spent(month=None):
    """Calcula cuánto se ha gastado en el mes actual o indicado (YYYY-MM)."""
    expenses = load_data()
    if not expenses:
        return 0
    if month is None:
        month = datetime.now().strftime("%Y-%m")
    total = sum(exp["amount"] for exp in expenses if exp["date"].startswith(month))
    return total

def check_budget_status():
    """Verifica si se ha superado el presupuesto."""
    budget_info = get_monthly_budget()
    budget = budget_info["budget"]
    if budget == 0:
        return "⚠️ No hay presupuesto establecido."
    spent = get_monthly_spent()
    if spent > budget:
        return f"🚨 Presupuesto superado: ${spent} / ${budget}"
    else:
        remaining = budget - spent
        return f"✅ Presupuesto OK. Gastado ${spent}, disponible ${remaining}"
