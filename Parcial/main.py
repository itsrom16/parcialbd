import time
from generador_datos import generar_productos
from ordenamientos import (
    insertion_sort_precio,
    merge_sort_calificacion,
    quick_sort_precio
)
from busquedas import (
    busqueda_binaria_id,
    busqueda_lineal_nombre
)

# Generar productos
productos = generar_productos()

print("=== LISTA ORIGINAL (5 productos aleatorios) ===")
for p in productos[:5]:
    print(p)

# 🕒 Insertion Sort (por precio)
inicio = time.time()
ordenados_precio_insertion = insertion_sort_precio(productos.copy())
fin = time.time()
print("\n=== ORDENADO POR PRECIO (Insertion Sort) ===")
for p in ordenados_precio_insertion[:5]:
    print(p)
print(f"⏱️ Tiempo: {fin - inicio:.6f} segundos")

# 🕒 Merge Sort (por calificación)
inicio = time.time()
ordenados_calificacion_merge = merge_sort_calificacion(productos.copy())
fin = time.time()
print("\n=== ORDENADO POR CALIFICACIÓN (Merge Sort) ===")
for p in ordenados_calificacion_merge[:5]:
    print(p)
print(f"⏱️ Tiempo: {fin - inicio:.6f} segundos")

# 🕒 Quick Sort (por precio)
inicio = time.time()
ordenados_precio_quick = quick_sort_precio(productos.copy())
fin = time.time()
print("\n=== ORDENADO POR PRECIO (Quick Sort) ===")
for p in ordenados_precio_quick[:5]:
    print(p)
print(f"⏱️ Tiempo: {fin - inicio:.6f} segundos")

# 🕒 Búsqueda binaria por ID
productos_ordenados_id = sorted(productos.copy(), key=lambda p: p.id)
id_a_buscar = 10
inicio = time.time()
resultado_id = busqueda_binaria_id(productos_ordenados_id, id_a_buscar)
fin = time.time()
print(f"\n=== BÚSQUEDA BINARIA POR ID ({id_a_buscar}) ===")
print("Resultado:", resultado_id if resultado_id else "Producto no encontrado.")
print(f"⏱️ Tiempo: {fin - inicio:.6f} segundos")

# 🕒 Búsqueda lineal por nombre
nombre_a_buscar = "laptop"
inicio = time.time()
resultados_nombre = busqueda_lineal_nombre(productos, nombre_a_buscar)
fin = time.time()
print(f"\n=== BÚSQUEDA LINEAL POR NOMBRE ('{nombre_a_buscar}') ===")
if resultados_nombre:
    for p in resultados_nombre:
        print(p)
else:
    print("No se encontraron productos.")
print(f"⏱️ Tiempo: {fin - inicio:.6f} segundos")
