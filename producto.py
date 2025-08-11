# Clase Producto representa un producto con ID único, nombre, cantidad y precio.
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        :param id_producto: Identificador único del producto (string o número)
        :param nombre: Nombre del producto
        :param cantidad: Cantidad disponible (entero)
        :param precio: Precio unitario (float)
        """
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Métodos getters para acceder a los atributos
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Métodos setters para modificar atributos
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def set_cantidad(self, nueva_cantidad):
        self._cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self._precio = nuevo_precio

    def __str__(self):
        """
        Representación amigable para imprimir el producto.
        """
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"
