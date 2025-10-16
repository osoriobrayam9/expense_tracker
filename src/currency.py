# Conversor simple de divisas sin conexión (tasas fijas aproximadas)
# COP = peso colombiano, USD = dólar, EUR = euro

EXCHANGE_RATES = {
    "COP": 1.0,
    "USD": 0.00025,  # 1 COP = 0.00025 USD
    "EUR": 0.00023,  # 1 COP = 0.00023 EUR
}

def convert_amount(amount_cop, target_currency="COP"):
    """Convierte un monto desde COP a la moneda indicada."""
    target_currency = target_currency.upper()
    if target_currency not in EXCHANGE_RATES:
        raise ValueError("Moneda no soportada. Use COP, USD o EUR.")
    return round(amount_cop * EXCHANGE_RATES[target_currency], 2)
