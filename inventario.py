from producto import Producto

# Clase Inventario para gestionar una lista de productos
class Inventario:
    def __init__(self):
        """
        Inicializa el inventario como una lista vacía.
        """
        self.productos = []

    def añadir_producto(self, producto):
        """
        Añade un producto al inventario si el ID es único.
        :param producto: instancia de Producto
        :return: True si se añade, False si el ID ya existe
        """
        # Verificamos si el ID ya está en la lista
        if any(p.get_id() == producto.get_id() for p in self.productos):
            return False  # No se añade producto con ID duplicado
        self.productos.append(producto)
        return True

    def eliminar_producto(self, id_producto):
        """
        Elimina producto según el ID.
        :param id_producto: ID del producto a eliminar
        :return: True si se elimina, False si no se encuentra
        """
        for i, p in enumerate(self.productos):
            if p.get_id() == id_producto:
                del self.productos[i]
                return True
        return False

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualiza cantidad y/o precio de un producto identificado por ID.
        :param id_producto: ID del producto
        :param cantidad: Nueva cantidad (opcional)
        :param precio: Nuevo precio (opcional)
        :return: True si se actualiza, False si no se encuentra
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                return True
        return False

    def buscar_productos(self, nombre_buscar):
        """
        Busca productos cuyo nombre contiene la cadena dada (case insensitive).
        :param nombre_buscar: Texto para buscar en el nombre
        :return: Lista de productos que coinciden
        """
        nombre_buscar = nombre_buscar.lower()
        return [p for p in self.productos if nombre_buscar in p.get_nombre().lower()]

    def mostrar_todos(self):
        """
        Devuelve la lista completa de productos en el inventario.
        """
        return self.productos
