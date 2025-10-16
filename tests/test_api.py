import json
import urllib.request
from src import api

def test_api_endpoints(monkeypatch):
    monkeypatch.setattr(api, "load_data", lambda: [{"description": "A", "amount": 10}])
    monkeypatch.setattr(api, "get_basic_statistics", lambda: {"avg": 10})
    msg = api.start_api_server(8081)
    assert "http" in msg

    with urllib.request.urlopen("http://127.0.0.1:8081/expenses") as r:
        data = json.loads(r.read())
        assert data["count"] == 1

    with urllib.request.urlopen("http://127.0.0.1:8081/stats") as r:
        data = json.loads(r.read())
        assert "avg" in data["stats"]

    msg2 = api.stop_api_server()
    assert "detenida" in msg2 or "API" in msg2
