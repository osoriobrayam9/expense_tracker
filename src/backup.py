import shutil
from pathlib import Path
from datetime import datetime

BACKUPS_DIR = Path("backups")
DATA_DIR = Path("data")

INCLUDE_ROOT = [
    Path("users.json"),
    Path("session.json"),
    Path("gastos.csv"),
    Path("app.log"),
]

def create_backup():
    BACKUPS_DIR.mkdir(exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    target_dir = BACKUPS_DIR / f"backup_{ts}"
    target_dir.mkdir(parents=True, exist_ok=True)

    # Copia archivos raíz seleccionados
    for p in INCLUDE_ROOT:
        if p.exists():
            shutil.copy2(p, target_dir / p.name)

    # Copia data/*.json
    if DATA_DIR.exists():
        (target_dir / "data").mkdir(exist_ok=True)
        for jf in DATA_DIR.glob("*.json"):
            shutil.copy2(jf, target_dir / "data" / jf.name)

    # Comprimir a ZIP
    zip_path = BACKUPS_DIR / f"backup_{ts}"
    shutil.make_archive(str(zip_path), "zip", target_dir)

    return f"{zip_path}.zip"
