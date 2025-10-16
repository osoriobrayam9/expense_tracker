from src.tracker import (
    add_expense,
    list_expenses,
    get_total_expense,
    get_expense_by_category,
    edit_expense,
    delete_expense,
    filter_by_date,
    filter_by_month,
    export_to_csv,
)
from src.validator import validate_amount, validate_date
from src.report import (
    get_average_daily_expense,
    get_average_monthly_expense,
    get_most_expensive_category,
    get_days_without_expense,
)
from src.currency import convert_amount

def menu():
    while True:
        print("\n=== GESTOR DE GASTOS PERSONALES ===")
        print("1. Agregar gasto")
        print("2. Listar todos los gastos")
        print("3. Total gastado")
        print("4. Gasto por categoría")
        print("5. Editar gasto")
        print("6. Eliminar gasto")
        print("7. Filtrar por fecha")
        print("8. Filtrar por mes")
        print("9. Exportar a CSV")
        print("10. Reportes avanzados")
        print("11. Conversor de moneda")
        print("12. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                desc = input("Descripción: ")
                cat = input("Categoría: ")
                amt = float(input("Monto: "))
                validate_amount(amt)
                fecha_input = input("Fecha (YYYY-MM-DD, vacío = hoy): ") or None
                if fecha_input:
                    validate_date(fecha_input)
                add_expense(desc, cat, amt, fecha_input)
                print("✅ Gasto agregado correctamente.")
            elif opcion == "2":
                expenses = list_expenses()
                if not expenses:
                    print("No hay gastos registrados.")
                else:
                    for i, e in enumerate(expenses):
                        print(f"{i}. {e['description']} ({e['category']}) - {e['date']}: ${e['amount']}")
            elif opcion == "3":
                print(f"💰 Total gastado: ${get_total_expense()}")
            elif opcion == "4":
                cat = input("Categoría: ")
                print(f"💸 Total en {cat}: ${get_expense_by_category(cat)}")
            elif opcion == "5":
                expenses = list_expenses()
                if not expenses:
                    print("No hay gastos para editar.")
                else:
                    for i, e in enumerate(expenses):
                        print(f"{i}. {e['description']} ({e['category']}) - {e['date']}: ${e['amount']}")
                    idx = int(input("Número del gasto a editar: "))
                    new_desc = input("Nueva descripción (vacío si no cambia): ") or None
                    new_cat = input("Nueva categoría (vacío si no cambia): ") or None
                    new_amt_input = input("Nuevo monto (vacío si no cambia): ")
                    new_amt = float(new_amt_input) if new_amt_input else None
                    if new_amt is not None:
                        validate_amount(new_amt)
                    new_date = input("Nueva fecha (YYYY-MM-DD, vacío si no cambia): ") or None
                    if new_date:
                        validate_date(new_date)
                    updated = edit_expense(idx, new_desc, new_cat, new_amt, new_date)
                    print(f"✅ Gasto actualizado: {updated}")
            elif opcion == "6":
                expenses = list_expenses()
                if not expenses:
                    print("No hay gastos para eliminar.")
                else:
                    for i, e in enumerate(expenses):
                        print(f"{i}. {e['description']} ({e['category']}) - {e['date']}: ${e['amount']}")
                    idx = int(input("Número del gasto a eliminar: "))
                    deleted = delete_expense(idx)
                    print(f"🗑️ Gasto eliminado: {deleted}")
            elif opcion == "7":
                date_str = input("Fecha (YYYY-MM-DD): ")
                validate_date(date_str)
                filtered = filter_by_date(date_str)
                if filtered:
                    print(f"\n📅 Gastos del {date_str}:")
                    for e in filtered:
                        print(f"- {e['description']} ({e['category']}): ${e['amount']}")
                else:
                    print("No se encontraron gastos en esa fecha.")
            elif opcion == "8":
                month_str = input("Mes (YYYY-MM): ")
                filtered = filter_by_month(month_str)
                if filtered:
                    print(f"\n📆 Gastos del mes {month_str}:")
                    for e in filtered:
                        print(f"- {e['description']} ({e['category']}) - {e['date']}: ${e['amount']}")
                else:
                    print("No se encontraron gastos en ese mes.")
            elif opcion == "9":
                filename = export_to_csv()
                print(f"📁 Exportado a {filename}")
            elif opcion == "10":
                print("\n📊 === REPORTES AVANZADOS ===")
                print(f"Promedio diario: ${get_average_daily_expense()}")
                print(f"Promedio mensual: ${get_average_monthly_expense()}")
                cat, val = get_most_expensive_category()
                print(f"Categoría con más gasto: {cat} (${val})")
                missing = get_days_without_expense()
                if missing:
                    print(f"Días sin gasto registrados ({len(missing)}): {', '.join(missing[:5])} ...")
                else:
                    print("No hay días sin gastos entre las fechas registradas.")
            elif opcion == "11":
                total_cop = get_total_expense()
                currency = input("Convertir a (USD/EUR/COP): ").upper()
                converted = convert_amount(total_cop, currency)
                print(f"💱 Total en {currency}: {converted}")
            elif opcion == "12":
                print("👋 Saliendo del programa...")
                break
            else:
                print("❌ Opción inválida. Intente nuevamente.")
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    menu()
