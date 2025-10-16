from src import charts

def test_chart_by_category(monkeypatch, capsys):
    mock_data = [
        {"category": "Comida", "amount": 100},
        {"category": "Transporte", "amount": 50},
    ]
    monkeypatch.setattr(charts, "load_data", lambda: mock_data)
    charts.chart_by_category()
    captured = capsys.readouterr()
    assert "Comida" in captured.out
    assert "Transporte" in captured.out
