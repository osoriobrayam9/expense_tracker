import json
from src import storage

def test_save_and_load_data(tmp_path):
    file = tmp_path / "expenses.json"
    data = [{"description": "Comida", "category": "Alimentos", "amount": 20}]
    storage.DATA_FILE = file

    storage.save_data(data)
    result = storage.load_data()

    assert result == data
