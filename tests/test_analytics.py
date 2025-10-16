from src import analytics

def test_basic_statistics(monkeypatch):
    mock_data = [{"amount": 10}, {"amount": 20}, {"amount": 30}]
    monkeypatch.setattr(analytics, "load_data", lambda: mock_data)
    stats = analytics.get_basic_statistics()
    assert stats["min"] == 10
    assert stats["max"] == 30
    assert "avg" in stats
    assert "std_dev" in stats
