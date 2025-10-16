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
from src.users import create_user, login, logout, get_current_user
from src.charts import chart_by_category, chart_by_month
from src.backup import create_backup
from src.api import start_api_server, stop_api_server

def _require_user():
    user = get_current_user()
    if not user:
        raise RuntimeError("No has iniciado sesión. Ve al menú de usuarios.")
    return user

def menu():
    while True:
        current = get_current_user() or "—"
        print(f"\n=== GESTOR DE GASTOS (Usuario: {current}) ===")
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
        print("12. Presupuesto mensual / Estado")
        print("13. Análisis estadístico")
        print("14. Alertas del sistema")
        print("15. Gráfico por categoría (ASCII)")
        print("16. Gráfico por mes (ASCII)")
        print("17. Backup (ZIP)")
        print("18. API local: iniciar")
        print("19. API local: detener")
        print("20. Usuarios: registrar")
        print("21. Usuarios: login")
        print("22. Usuarios: logout")
        print("23. Salir")

        op = input("Seleccione una opción: ")

        try:
            if op == "1":
                _require_user()
                desc = input("Descripción: ")
                cat = input("Categoría: ")
                amt = float(input("Monto: "))
                validate_amount(amt)
                fecha = input("Fecha (YYYY-MM-DD, vacío = hoy): ") or None
                if fecha:
                    validate_date(fecha)
                add_expense(desc, cat, amt, fecha)
                log_action("Nuevo gasto", f"{desc} - {cat} - ${amt}")
                print("✅ Gasto agregado.")

            elif op == "2":
                _require_user()
                items = list_expenses()
                if not items:
                    print("No hay gastos.")
                else:
                    for i, e in enumerate(items):
                        print(f"{i}. {e['description']} ({e['category']}) - {e['date']}: ${e['amount']}")

            elif op == "3":
                _require_user()
                print(f"💰 Total: ${get_total_expense()}")

            elif op == "4":
                _require_user()
                cat = input("Categoría: ")
                print(f"💸 Total en {cat}: ${get_expense_by_category(cat)}")

            elif op == "5":
                _require_user()
                idx = int(input("Índice a editar: "))
                new_desc = input("Nueva descripción (vacío = igual): ") or None
                new_cat = input("Nueva categoría (vacío = igual): ") or None
                new_amt_str = input("Nuevo monto (vacío = igual): ")
                new_amt = float(new_amt_str) if new_amt_str else None
                if new_amt is not None:
                    validate_amount(new_amt)
                new_date = input("Nueva fecha (YYYY-MM-DD, vacío = igual): ") or None
                if new_date:
                    validate_date(new_date)
                updated = edit_expense(idx, new_desc, new_cat, new_amt, new_date)
                log_action("Editar gasto", f"{updated}")
                print("✅ Actualizado.")

            elif op == "6":
                _require_user()
                idx = int(input("Índice a eliminar: "))
                deleted = delete_expense(idx)
                log_action("Eliminar gasto", f"{deleted}")
                print("🗑️ Eliminado.")

            elif op == "7":
                _require_user()
                d = input("Fecha (YYYY-MM-DD): ")
                validate_date(d)
                for e in filter_by_date(d):
                    print(f"- {e['description']} ({e['category']}): ${e['amount']}")

            elif op == "8":
                _require_user()
                m = input("Mes (YYYY-MM): ")
                for e in filter_by_month(m):
                    print(f"- {e['description']} ({e['category']}) - {e['date']}: ${e['amount']}")

            elif op == "9":
                _require_user()
                fn = export_to_csv()
                print(f"📁 Exportado a {fn}")

            elif op == "10":
                _require_user()
                print("\n📊 === REPORTES ===")
                print(f"Promedio diario: ${get_average_daily_expense()}")
                print(f"Promedio mensual: ${get_average_monthly_expense()}")
                cat, val = get_most_expensive_category()
                print(f"Categoría con más gasto: {cat} (${val})")
                missing = get_days_without_expense()
                print(f"Días sin gasto (entre min y max): {len(missing)}")

            elif op == "11":
                _require_user()
                total = get_total_expense()
                curr = input("Moneda destino (USD/EUR/COP): ").upper()
                print(f"💱 {curr}: {convert_amount(total, curr)}")

            elif op == "12":
                _require_user()
                print("\n💼 === PRESUPUESTO ===")
                sub = input("[1] Establecer  [2] Ver estado: ")
                if sub == "1":
                    val = float(input("Nuevo presupuesto mensual: "))
                    validate_amount(val)
                    from src.budget import set_monthly_budget
                    data = set_monthly_budget(val)
                    print(f"✅ Presupuesto: ${data['budget']} (desde {data['last_updated']})")
                print(check_budget_status())

            elif op == "13":
                _require_user()
                print("\n📈 === ESTADÍSTICAS ===")
                stats = get_basic_statistics()
                for k, v in stats.items():
                    print(f"{k.capitalize()}: {v}")

            elif op == "14":
                _require_user()
                print("\n🔔 === ALERTAS ===")
                for a in system_alerts():
                    print(a)

            elif op == "15":
                _require_user()
                chart_by_category()

            elif op == "16":
                _require_user()
                chart_by_month()

            elif op == "17":
                # backup no requiere sesión, pero es útil tener el contexto
                z = create_backup()
                print(f"🧰 Backup creado: {z}")

            elif op == "18":
                msg = start_api_server()
                print(f"🌐 {msg}")

            elif op == "19":
                msg = stop_api_server()
                print(f"🛑 {msg}")

            elif op == "20":
                username = input("Nuevo usuario: ")
                full = input("Nombre completo: ")
                pwd = input("Contraseña: ")
                u = create_user(username, full, pwd)
                print(f"✅ Usuario creado: {u['username']}")

            elif op == "21":
                username = input("Usuario: ")
                pwd = input("Contraseña: ")
                who = login(username, pwd)
                print(f"✅ Sesión iniciada como {who}")

            elif op == "22":
                logout()
                print("✅ Sesión cerrada.")

            elif op == "23":
                print("👋 Saliendo...")
                break

            else:
                print("❌ Opción inválida.")

        except Exception as e:
            log_error(str(e))
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    menu()
