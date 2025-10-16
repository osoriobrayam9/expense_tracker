import pytest
from src import validator

def test_validate_amount_accepts_positive():
    """Debe aceptar montos positivos sin lanzar error."""
    validator.validate_amount(10)  # No debe lanzar excepción

def test_validate_amount_rejects_negative():
    """Debe lanzar ValueError cuando el monto es negativo."""
    with pytest.raises(ValueError):
        validator.validate_amount(-5)

def test_validate_date_valid_format():
    """Debe aceptar una fecha válida en formato YYYY-MM-DD."""
    validator.validate_date("2025-10-16")  # No debe lanzar error

def test_validate_date_invalid_format():
    """Debe lanzar ValueError si la fecha tiene formato incorrecto."""
    with pytest.raises(ValueError):
        validator.validate_date("16/10/2025")
