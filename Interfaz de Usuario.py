from producto import Producto
from inventario import Inventario

def menu():
    inventario = Inventario()  # Creamos el inventario vacío

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Añadir producto pidiendo datos al usuario
            id_producto = input("Ingrese ID único del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            try:
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
            except ValueError:
                print("Error: Cantidad debe ser entero y precio número decimal.")
                continue

            producto = Producto(id_producto, nombre, cantidad, precio)
            if inventario.añadir_producto(producto):
                print("Producto añadido correctamente.")
            else:
                print("Error: Ya existe un producto con ese ID.")

        elif opcion == "2":
            # Eliminar producto por ID
            id_producto = input("Ingrese ID del producto a eliminar: ")
            if inventario.eliminar_producto(id_producto):
                print("Producto eliminado correctamente.")
            else:
                print("No se encontró producto con ese ID.")

        elif opcion == "3":
            # Actualizar producto (cantidad y/o precio)
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad_input = input("Nueva cantidad (deje vacío si no cambia): ")
            precio_input = input("Nuevo precio (deje vacío si no cambia): ")

            cantidad = int(cantidad_input) if cantidad_input else None
            precio = float(precio_input) if precio_input else None

            if inventario.actualizar_producto(id_producto, cantidad, precio):
                print("Producto actualizado correctamente.")
            else:
                print("No se encontró producto con ese ID.")

        elif opcion == "4":
            # Buscar productos por nombre
            nombre_buscar = input("Ingrese nombre o parte del nombre a buscar: ")
            resultados = inventario.buscar_productos(nombre_buscar)
            if resultados:
                print(f"Se encontraron {len(resultados)} producto(s):")
                for prod in resultados:
                    print(prod)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            # Mostrar todos los productos
            productos = inventario.mostrar_todos()
            if productos:
                print("Lista de productos en inventario:")
                for prod in productos:
                    print(prod)
            else:
                print("El inventario está vacío.")

        elif opcion == "6":
            # Salir del programa
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
