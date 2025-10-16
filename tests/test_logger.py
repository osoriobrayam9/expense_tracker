from pathlib import Path
from src import logger

def test_log_action_and_error(tmp_path, monkeypatch):
    log_file = tmp_path / "app.log"
    monkeypatch.setattr(logger, "LOG_FILE", log_file)
    logger.log_action("TEST_ACTION", "Se realizó algo")
    logger.log_error("Error simulado")
    # Verificar que el archivo existe y contiene ambos mensajes
    content = log_file.read_text(encoding="utf-8")
    assert "TEST_ACTION" in content
    assert "Error simulado" in content
