from pathlib import Path
from src import backup

def test_create_backup(tmp_path, monkeypatch):
    monkeypatch.setattr(backup, "BACKUPS_DIR", tmp_path / "backups")
    (tmp_path / "users.json").write_text("{}", encoding="utf-8")
    (tmp_path / "session.json").write_text("{}", encoding="utf-8")
    monkeypatch.setattr(backup, "INCLUDE_ROOT", [tmp_path / "users.json", tmp_path / "session.json"])
    zip_path = backup.create_backup()
    assert zip_path.endswith(".zip")
    assert Path(zip_path).exists()
