from src.tracker import (
    add_expense,
    list_expenses,
    get_total_expense,
    get_expense_by_category,
    edit_expense,
    delete_expense,
    filter_by_date,
    filter_by_month,
)

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
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            desc = input("Descripción: ")
            cat = input("Categoría: ")
            amt = float(input("Monto: "))
            fecha_input = input("Fecha (YYYY-MM-DD, vacío = hoy): ") or None
            add_expense(desc, cat, amt, fecha_input)
            print("✅ Gasto agregado.")
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
                try:
                    idx = int(input("Ingrese el número del gasto a editar: "))
                    new_desc = input("Nueva descripción (vacío si no cambia): ") or None
                    new_cat = input("Nueva categoría (vacío si no cambia): ") or None
                    new_amt_input = input("Nuevo monto (vacío si no cambia): ")
                    new_amt = float(new_amt_input) if new_amt_input else None
                    new_date = input("Nueva fecha (YYYY-MM-DD, vacío si no cambia): ") or None
                    updated = edit_expense(idx, new_desc, new_cat, new_amt, new_date)
                    print(f"✅ Gasto actualizado: {updated}")
                except (ValueError, IndexError) as e:
                    print(f"⚠️ Error: {e}")
        elif opcion == "6":
            expenses = list_expenses()
            if not expenses:
                print("No hay gastos para eliminar.")
            else:
                for i, e in enumerate(expenses):
                    print(f"{i}. {e['description']} ({e['category']}) - {e['date']}: ${e['amount']}")
                try:
                    idx = int(input("Ingrese el número del gasto a eliminar: "))
                    deleted = delete_expense(idx)
                    print(f"🗑️ Gasto eliminado: {deleted}")
                except (ValueError, IndexError) as e:
                    print(f"⚠️ Error: {e}")
        elif opcion == "7":
            date_str = input("Ingrese la fecha (YYYY-MM-DD): ")
            filtered = filter_by_date(date_str)
            if filtered:
                print(f"\n📅 Gastos del {date_str}:")
                for e in filtered:
                    print(f"- {e['description']} ({e['category']}): ${e['amount']}")
            else:
                print("No se encontraron gastos en esa fecha.")
        elif opcion == "8":
            month_str = input("Ingrese el mes (YYYY-MM): ")
            filtered = filter_by_month(month_str)
            if filtered:
                print(f"\n📆 Gastos del mes {month_str}:")
                for e in filtered:
                    print(f"- {e['description']} ({e['category']}) - {e['date']}: ${e['amount']}")
            else:
                print("No se encontraron gastos en ese mes.")
        elif opcion == "9":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
