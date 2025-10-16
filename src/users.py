import json
import hashlib
from pathlib import Path
from datetime import datetime

USERS_FILE = Path("users.json")
SESSION_FILE = Path("session.json")
DATA_DIR = Path("data")

def _load_json(path: Path, default):
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default

def _save_json(path: Path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def _hash_password(username: str, password: str) -> str:
    # Hash simple con “sal” del username
    combo = f"{username}:{password}".encode("utf-8")
    return hashlib.sha256(combo).hexdigest()

def create_user(username: str, full_name: str, password: str):
    username = username.strip()
    users = _load_json(USERS_FILE, {})
    if username in users:
        raise ValueError("El usuario ya existe.")
    pwd = _hash_password(username, password)
    users[username] = {
        "full_name": full_name,
        "password_hash": pwd,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    _save_json(USERS_FILE, users)
    # Prepara archivo de gastos del usuario
    DATA_DIR.mkdir(exist_ok=True)
    get_expenses_file_for_user(username).touch(exist_ok=True)
    return {"username": username, "full_name": full_name}

def authenticate(username: str, password: str) -> bool:
    users = _load_json(USERS_FILE, {})
    if username not in users:
        return False
    return users[username]["password_hash"] == _hash_password(username, password)

def login(username: str, password: str):
    if not authenticate(username, password):
        raise ValueError("Credenciales inválidas.")
    _save_json(SESSION_FILE, {"current_user": username})
    return username

def logout():
    if SESSION_FILE.exists():
        SESSION_FILE.unlink()

def get_current_user() -> str | None:
    data = _load_json(SESSION_FILE, {})
    return data.get("current_user")

def get_expenses_file_for_user(username: str) -> Path:
    return DATA_DIR / f"{username}_expenses.json"
