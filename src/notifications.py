from datetime import datetime, timedelta
from src.storage import load_data
from src.budget import check_budget_status

def get_last_expense_date():
    """Devuelve la fecha del último gasto registrado."""
    expenses = load_data()
    if not expenses:
        return None
    last = max(exp["date"] for exp in expenses)
    return last

def check_inactivity_alert(days=3):
    """Alerta si no se han registrado gastos en los últimos N días."""
    last_date = get_last_expense_date()
    if not last_date:
        return "⚠️ No hay gastos registrados."
    last_dt = datetime.strptime(last_date, "%Y-%m-%d")
    diff = (datetime.now() - last_dt).days
    if diff >= days:
        return f"🔕 No registras gastos hace {diff} días."
    else:
        return "✅ Actividad reciente registrada."

def system_alerts():
    """Combina alertas de presupuesto e inactividad."""
    alerts = []
    alerts.append(check_budget_status())
    alerts.append(check_inactivity_alert())
    return alerts
