import logging
from datetime import datetime

LOG_FILE = "app.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def log_action(action, details=""):
    """Registra una acción en el log."""
    logging.info(f"{action}: {details}")

def log_error(error_message):
    """Registra un error."""
    logging.error(error_message)
