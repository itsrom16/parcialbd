# ordenamientos.py

def insertion_sort_precio(productos):
    for i in range(1, len(productos)):
        actual = productos[i]
        j = i - 1
        while j >= 0 and productos[j].precio > actual.precio:
            productos[j + 1] = productos[j]
            j -= 1
        productos[j + 1] = actual
    return productos


def merge_sort_calificacion(productos):
    if len(productos) <= 1:
        return productos

    medio = len(productos) // 2
    izquierda = merge_sort_calificacion(productos[:medio])
    derecha = merge_sort_calificacion(productos[medio:])

    return merge_calificacion(izquierda, derecha)

def merge_calificacion(izquierda, derecha):
    resultado = []
    while izquierda and derecha:
        if izquierda[0].calificacion_promedio > derecha[0].calificacion_promedio:
            resultado.append(izquierda.pop(0))
        else:
            resultado.append(derecha.pop(0))
    resultado.extend(izquierda or derecha)
    return resultado


def quick_sort_precio(productos):
    if len(productos) <= 1:
        return productos

    pivote = productos[0]
    menores = [p for p in productos[1:] if p.precio < pivote.precio]
    iguales = [p for p in productos if p.precio == pivote.precio]
    mayores = [p for p in productos[1:] if p.precio > pivote.precio]

    return quick_sort_precio(menores) + iguales + quick_sort_precio(mayores)
