class Producto:
    def __init__(self, id, nombre, precio, categoria, stock, calificacion_promedio):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
        self.calificacion_promedio = calificacion_promedio

    def __str__(self):
        return f"ID: {self.id} | {self.nombre} | ${self.precio:.2f} | {self.categoria} | Stock: {self.stock} | ⭐ {self.calificacion_promedio:.1f}"
