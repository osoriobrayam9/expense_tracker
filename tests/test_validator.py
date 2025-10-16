import pytest
from src import validator

def test_validate_amount_accepts_positive():
    validator.validate_amount(10)  # No debe lanzar error

def test_validate_amount_rejects_negative():
    with pytest.raises(ValueError):
        validator.validate_amount(-5)

def test_validate_date_valid_format():
    validator.validate_date("2025-10-16")  # No debe lanzar error

def test_validate_date_invalid_format():
    with pytest.raises(ValueError):
        validator.validate_date("16/10/2025")
