import json
from pathlib import Path
from src.users import get_current_user, get_expenses_file_for_user

DEFAULT_FILE = Path("expenses.json")

def _get_data_file() -> Path:
    user = get_current_user()
    if user:
        return get_expenses_file_for_user(user)
    return DEFAULT_FILE

def load_data():
    data_file = _get_data_file()
    if data_file.exists():
        with open(data_file, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return []
            return data
    return []

def save_data(expenses):
    data_file = _get_data_file()
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=4)
