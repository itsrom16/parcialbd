# busquedas.py

def busqueda_binaria_id(productos, id_busqueda):
    izquierda = 0
    derecha = len(productos) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if productos[medio].id == id_busqueda:
            return productos[medio]
        elif productos[medio].id < id_busqueda:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None


def busqueda_lineal_nombre(productos, nombre_busqueda):
    nombre_busqueda = nombre_busqueda.lower()
    resultados = []

    for producto in productos:
        if nombre_busqueda in producto.nombre.lower():
            resultados.append(producto)

    return resultados
