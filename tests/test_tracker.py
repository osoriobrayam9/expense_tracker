import pytest
from src import tracker, storage, users

@pytest.fixture(autouse=True)
def clean_environment(tmp_path, monkeypatch):
    # Simular entorno temporal y usuario activo
    monkeypatch.setattr(users, "get_current_user", lambda: "testuser")
    monkeypatch.setattr(users, "get_expenses_file_for_user", lambda u: tmp_path / f"{u}_expenses.json")
    monkeypatch.setattr(storage, "_get_data_file", lambda: tmp_path / "expenses.json")
    yield

def test_add_and_list_expense(tmp_path):
    tracker.add_expense("Taxi", "Transporte", 15)
    expenses = tracker.list_expenses()
    assert len(expenses) == 1
    assert expenses[0]["category"] == "Transporte"
    assert expenses[0]["amount"] == 15

def test_total_and_category(tmp_path):
    tracker.add_expense("Pan", "Comida", 2)
    tracker.add_expense("Leche", "Comida", 3)
    tracker.add_expense("Bus", "Transporte", 5)
    total = tracker.get_total_expense()
    comida = tracker.get_expense_by_category("Comida")
    assert total == 10
    assert comida == 5
