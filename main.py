from src.tracker import add_expense, list_expenses, get_total_expense, get_expense_by_category

def menu():
    while True:
        print("\n=== GESTOR DE GASTOS PERSONALES ===")
        print("1. Agregar gasto")
        print("2. Listar gastos")
        print("3. Total gastado")
        print("4. Gasto por categoría")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            desc = input("Descripción: ")
            cat = input("Categoría: ")
            amt = float(input("Monto: "))
            add_expense(desc, cat, amt)
            print("✅ Gasto agregado.")
        elif opcion == "2":
            for e in list_expenses():
                print(f"- {e['description']} ({e['category']}): ${e['amount']}")
        elif opcion == "3":
            print(f"💰 Total gastado: ${get_total_expense()}")
        elif opcion == "4":
            cat = input("Categoría: ")
            print(f"💸 Total en {cat}: ${get_expense_by_category(cat)}")
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
