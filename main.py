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
from src.budget import set_monthly_budget, check_budget_status
from src.analytics import get_basic_statistics
from src.notifications import system_alerts
from src.logger import log_action, log_error

def menu():
    while True:
        print("\n=== GESTOR DE GASTOS PERSONALES (Versión Avanzada) ===")
        print("1. Agregar gasto")
        print("2. Listar gastos")
        print("3. Total gastado")
        print("4. Gasto por categoría")
        print("5. Editar gasto")
        print("6. Eliminar gasto")
        print("7. Filtrar por fecha")
        print("8. Filtrar por mes")
        print("9. Exportar a CSV")
        print("10. Reportes avanzados")
        print("11. Conversor de moneda")
        print("12. Presupuesto mensual")
        print("13. Análisis estadístico")
        print("14. Alertas del sistema")
        print("15. Salir")

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
                log_action("Nuevo gasto agregado", f"{desc} - {cat} - ${amt}")
                print("✅ Gasto agregado correctamente.")

            elif opcion == "2":
                expenses = list_expenses()
                if not expenses:
                    print("No hay gastos registrados.")
                else:
                    for i, e in enumerate(expenses):
                        print(f"{i}. {e['description']} ({e['category']}) - {e['date']}: ${e['amount']}")

            elif opcion == "3":
                total = get_total_expense()
                print(f"💰 Total gastado: ${total}")

            elif opcion == "4":
                cat = input("Categoría: ")
                print(f"💸 Total en {cat}: ${get_expense_by_category(cat)}")

            elif opcion == "5":
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
                log_action("Gasto editado", f"{updated}")
                print("✅ Gasto actualizado.")

            elif opcion == "6":
                idx = int(input("Número del gasto a eliminar: "))
                deleted = delete_expense(idx)
                log_action("Gasto eliminado", f"{deleted}")
                print(f"🗑️ Eliminado: {deleted}")

            elif opcion == "7":
                date_str = input("Fecha (YYYY-MM-DD): ")
                validate_date(date_str)
                filtered = filter_by_date(date_str)
                for e in filtered:
                    print(f"- {e['description']} ({e['category']}): ${e['amount']}")

            elif opcion == "8":
                month_str = input("Mes (YYYY-MM): ")
                filtered = filter_by_month(month_str)
                for e in filtered:
                    print(f"- {e['description']} ({e['category']}) - {e['date']}: ${e['amount']}")

            elif opcion == "9":
                filename = export_to_csv()
                print(f"📁 Exportado a {filename}")

            elif opcion == "10":
                print("\n📊 === REPORTES ===")
                print(f"Promedio diario: ${get_average_daily_expense()}")
                print(f"Promedio mensual: ${get_average_monthly_expense()}")
                cat, val = get_most_expensive_category()
                print(f"Categoría con más gasto: {cat} (${val})")

            elif opcion == "11":
                total = get_total_expense()
                currency = input("Convertir a (USD/EUR/COP): ").upper()
                converted = convert_amount(total, currency)
                print(f"💱 Total en {currency}: {converted}")

            elif opcion == "12":
                print("\n💼 === PRESUPUESTO ===")
                amount = float(input("Nuevo presupuesto mensual: "))
                validate_amount(amount)
                data = set_monthly_budget(amount)
                print(f"✅ Presupuesto actualizado: ${data['budget']} (desde {data['last_updated']})")
                print(check_budget_status())

            elif opcion == "13":
                print("\n📈 === ANÁLISIS ESTADÍSTICO ===")
                stats = get_basic_statistics()
                for k, v in stats.items():
                    print(f"{k.capitalize()}: {v}")

            elif opcion == "14":
                print("\n🔔 === ALERTAS ===")
                for alert in system_alerts():
                    print(alert)

            elif opcion == "15":
                print("👋 Saliendo del sistema...")
                break

            else:
                print("❌ Opción inválida.")

        except Exception as e:
            log_error(str(e))
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    menu()
