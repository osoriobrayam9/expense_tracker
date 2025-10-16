from src import budget

def test_set_and_check_budget(tmp_path, monkeypatch):
    monkeypatch.setattr(budget, "BUDGET_FILE", tmp_path / "budget.json")
    monkeypatch.setattr(budget, "load_data", lambda: [
        {"amount": 100, "date": "2025-10-10"},
        {"amount": 50, "date": "2025-10-12"},
    ])
    budget.set_monthly_budget(200)
    status = budget.check_budget_status()
    assert "Presupuesto" in status
