from src import storage, users

def test_save_and_load_with_user(tmp_path, monkeypatch):
    monkeypatch.setattr(users, "get_current_user", lambda: "testuser")
    monkeypatch.setattr(users, "get_expenses_file_for_user", lambda u: tmp_path / f"{u}_expenses.json")

    data = [{"description": "Almuerzo", "category": "Comida", "amount": 15, "date": "2025-10-16"}]
    storage.save_data(data)
    result = storage.load_data()
    assert result == data
