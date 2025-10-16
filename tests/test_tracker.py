from src import tracker, storage

def test_add_and_list_expense(tmp_path):
    file = tmp_path / "expenses.json"
    storage.DATA_FILE = file

    tracker.add_expense("Taxi", "Transporte", 15)
    expenses = tracker.list_expenses()

    assert len(expenses) == 1
    assert expenses[0]["category"] == "Transporte"

def test_total_and_category(tmp_path):
    file = tmp_path / "expenses.json"
    storage.DATA_FILE = file
    tracker.add_expense("Pan", "Comida", 2)
    tracker.add_expense("Leche", "Comida", 3)
    tracker.add_expense("Bus", "Transporte", 5)

    assert tracker.get_total_expense() == 10
    assert tracker.get_expense_by_category("Comida") == 5
