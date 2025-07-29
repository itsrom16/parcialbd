import random
from producto import Producto

nombres = ["Camisa", "Laptop", "Libro", "Silla", "Zapatos", "Audífonos", "Mochila", "Celular", "Monitor", "Cargador"]
categorias = ["Electrónica", "Ropa", "Libros", "Hogar"]

def generar_productos(cantidad=50):
    productos = []
    for i in range(1, cantidad + 1):
        nombre = random.choice(nombres) + f" {random.randint(1, 100)}"
        precio = round(random.uniform(10.0, 1000.0), 2)
        categoria = random.choice(categorias)
        stock = random.randint(0, 100)
        calificacion = round(random.uniform(1.0, 5.0), 1)
        producto = Producto(i, nombre, precio, categoria, stock, calificacion)
        productos.append(producto)
    return productos
