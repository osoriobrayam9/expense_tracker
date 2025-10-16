import pytest
import builtins
from src import tracker, storage, users

@pytest.fixture(autouse=True)
def clean_environment(tmp_path, monkeypatch):
    """Crea entorno temporal y usuario simulado."""
    monkeypatch.setattr(users, "get_current_user", lambda: "testuser")
    monkeypatch.setattr(users, "get_expenses_file_for_user", lambda u: tmp_path / f"{u}_expenses.json")
    monkeypatch.setattr(storage, "_get_data_file", lambda: tmp_path / "expenses.json")
    yield


def test_add_and_list_expense():
    """Debe agregar y listar correctamente un gasto."""
    tracker.add_expense("Taxi", "Transporte", 15)
    expenses = tracker.list_expenses()
    assert len(expenses) == 1
    assert expenses[0]["description"] == "Taxi"
    assert expenses[0]["amount"] == 15


def test_total_and_category():
    """Debe calcular correctamente el total y los gastos por categoría."""
    tracker.add_expense("Pan", "Comida", 2)
    tracker.add_expense("Leche", "Comida", 3)
    tracker.add_expense("Bus", "Transporte", 5)
    total = tracker.get_total_expense()
    comida = tracker.get_expense_by_category("Comida")
    assert total == 10
    assert comida == 5


def test_edit_expense():
    """Debe permitir editar correctamente un gasto existente."""
    tracker.add_expense("Helado", "Comida", 10)
    tracker.edit_expense(0, "Pizza", "Comida", 20)
    data = tracker.list_expenses()
    assert data[0]["description"] == "Pizza"
    assert data[0]["amount"] == 20


def test_delete_expense():
    """Debe eliminar correctamente un gasto del registro."""
    tracker.add_expense("Cine", "Entretenimiento", 25)
    tracker.add_expense("Bus", "Transporte", 5)
    tracker.delete_expense(0)
    data = tracker.list_expenses()
    assert len(data) == 1
    assert data[0]["description"] == "Bus"


def test_export_to_csv(tmp_path, monkeypatch):
    """Debe exportar los gastos actuales a un archivo CSV correctamente."""
    tracker.add_expense("Tienda", "Compras", 100)

    csv_path = tmp_path / "export.csv"

    # Guardar referencia original de open()
    original_open = builtins.open

    # Mock seguro de open() que evita recursión infinita
    def mock_open(file, mode="w", encoding=None, newline=None):
        # Redirige solo si se está escribiendo un CSV
        if str(file).endswith(".csv"):
            return original_open(csv_path, mode=mode, encoding=encoding, newline=newline)
        return original_open(file, mode=mode, encoding=encoding, newline=newline)

    monkeypatch.setattr(builtins, "open", mock_open)

    # Ejecutar la exportación
    tracker.export_to_csv()

    # Verificar que el archivo CSV fue creado
    assert csv_path.exists()
    content = csv_path.read_text(encoding="utf-8")
    assert "Tienda" in content
    assert "Compras" in content
