import statistics
from src.storage import load_data

def get_basic_statistics():
    """Devuelve datos estadísticos de los montos de gastos."""
    expenses = load_data()
    if not expenses:
        return {"min": 0, "max": 0, "avg": 0, "std_dev": 0}
    amounts = [exp["amount"] for exp in expenses]
    stats = {
        "min": min(amounts),
        "max": max(amounts),
        "avg": round(statistics.mean(amounts), 2),
        "std_dev": round(statistics.pstdev(amounts), 2),
    }
    return stats
