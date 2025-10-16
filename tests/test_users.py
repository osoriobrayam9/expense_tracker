import pytest
from pathlib import Path
from src import users

@pytest.fixture(autouse=True)
def clean_files(tmp_path, monkeypatch):
    monkeypatch.setattr(users, "USERS_FILE", tmp_path / "users.json")
    monkeypatch.setattr(users, "SESSION_FILE", tmp_path / "session.json")
    monkeypatch.setattr(users, "DATA_DIR", tmp_path)
    yield

def test_create_and_login_user():
    info = users.create_user("juan", "Juan Pérez", "1234")
    assert info["username"] == "juan"

    ok = users.authenticate("juan", "1234")
    assert ok is True

    who = users.login("juan", "1234")
    assert who == "juan"
    assert users.get_current_user() == "juan"

def test_logout_clears_session():
    users.create_user("maria", "María", "abc")
    users.login("maria", "abc")
    users.logout()
    assert users.get_current_user() is None
