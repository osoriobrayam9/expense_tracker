from src.tracker import (
    add_expense,
    list_expenses,
    get_total_expense,
    get_expense_by_category,
    edit_expense,
    delete_expense,
)

def menu():
    while True:
        print("\n=== GESTOR DE GASTOS PERSONALES ===")
        print("1. Agregar gasto")
        print("2. Listar gastos")
        print("3. Total gastado")
        print("4. Gasto por categoría")
        print("5. Editar gasto")
        print("6. Eliminar gasto")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            desc = input("Descripción: ")
            cat = input("Categoría: ")
            amt = float(input("Monto: "))
            add_expense(desc, cat, amt)
            print("✅ Gasto agregado.")
        elif opcion == "2":
            expenses = list_expenses()
            if not expenses:
                print("No hay gastos registrados.")
            else:
                for i, e in enumerate(expenses):
                    print(f"{i}. {e['description']} ({e['category']}): ${e['amount']}")
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
                    print(f"{i}. {e['description']} ({e['category']}): ${e['amount']}")
                try:
                    idx = int(input("Ingrese el número del gasto a editar: "))
                    new_desc = input("Nueva descripción (deje vacío si no cambia): ") or None
                    new_cat = input("Nueva categoría (deje vacío si no cambia): ") or None
                    new_amt_input = input("Nuevo monto (deje vacío si no cambia): ")
                    new_amt = float(new_amt_input) if new_amt_input else None
                    updated = edit_expense(idx, new_desc, new_cat, new_amt)
                    print(f"✅ Gasto actualizado: {updated}")
                except (ValueError, IndexError) as e:
                    print(f"⚠️ Error: {e}")
        elif opcion == "6":
            expenses = list_expenses()
            if not expenses:
                print("No hay gastos para eliminar.")
            else:
                for i, e in enumerate(expenses):
                    print(f"{i}. {e['description']} ({e['category']}): ${e['amount']}")
                try:
                    idx = int(input("Ingrese el número del gasto a eliminar: "))
                    deleted = delete_expense(idx)
                    print(f"🗑️ Gasto eliminado: {deleted}")
                except (ValueError, IndexError) as e:
                    print(f"⚠️ Error: {e}")
        elif opcion == "7":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
