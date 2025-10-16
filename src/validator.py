from datetime import datetime

def validate_amount(amount):
    """Verifica que el monto sea positivo."""
    if amount < 0:
        raise ValueError("El monto debe ser un número positivo.")

def validate_date(date_str):
    """Valida que la fecha esté en formato YYYY-MM-DD."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Formato de fecha inválido. Use YYYY-MM-DD.")
