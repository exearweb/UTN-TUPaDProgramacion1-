# 1. Crear archivo productos.txt con tres productos. Cada linea debe tener nombre, precio y cantidad.
with open("productos.txt", "w") as archivo:
    archivo.write("Manzanas,250,30\n")
    archivo.write("Bananas,180,25\n")
    archivo.write("Naranjas,220,40\n")

print("Archivo 'productos.txt' creado correctamente.")

# 2. Abrir y leer el archivo productos.txt
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        # Quitar espacios y saltos de línea, y separar por comas
        datos = linea.strip().split(",")
        
        # Asignar cada parte a una variable
        producto = datos[0]
        precio = datos[1]
        cantidad = datos[2]
        
        # Mostrar el formato solicitado
        print(f"Producto: {producto} | Precio: ${precio} | Cantidad: {cantidad}")

# 3. Abrir y leer el archivo productos.txt
with open("productos.txt", "r") as archivo:
    print("=== LISTA DE PRODUCTOS ===")
    for linea in archivo:
        # Quitar espacios y saltos de línea, y separar por comas
        datos = linea.strip().split(",")
        producto = datos[0]
        precio = datos[1]
        cantidad = datos[2]
        print(f"Producto: {producto} | Precio: ${precio} | Cantidad: {cantidad}")

# 4. Pedir al usuario que ingrese un nombre de producto
# Abrir y leer el archivo productos.txt
with open("productos.txt", "r") as archivo:
    print("=== LISTA DE PRODUCTOS ===")
    for linea in archivo:
        # Quitar espacios y saltos de línea, y separar por comas
        datos = linea.strip().split(",")
        producto = datos[0]
        precio = datos[1]
        cantidad = datos[2]
        print(f"Producto: {producto} | Precio: ${precio} | Cantidad: {cantidad}")

productos = []  # Lista vacía para almacenar los productos

# 5. Leer el archivo productos.txt
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        nombre = datos[0]
        precio = float(datos[1])
        cantidad = int(datos[2])
        
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        productos.append(producto)

# Mostrar los productos cargados
print("=== PRODUCTOS DISPONIBLES ===")
for p in productos:
    print(f"- {p['nombre']}")

# Buscar un producto por nombre
buscado = input("\nIngrese el nombre del producto que desea buscar: ").strip()

encontrado = False
for p in productos:
    if p["nombre"].lower() == buscado.lower():  # Comparación sin distinguir mayúsculas
        print(f"\n Producto encontrado:")
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: ${p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("\n El producto no existe en la lista.")

#6 Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista.
productos = []  # Lista de productos

# === LECTURA DEL ARCHIVO ===
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        nombre = datos[0]
        precio = float(datos[1])
        cantidad = int(datos[2])
        
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        productos.append(producto)

# === MOSTRAR PRODUCTOS ACTUALES ===
print("=== PRODUCTOS ACTUALES ===")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

# === AGREGAR NUEVO PRODUCTO ===
print("\n=== AGREGAR NUEVO PRODUCTO ===")
nuevo_nombre = input("Nombre: ").strip()
nuevo_precio = float(input("Precio: "))
nueva_cantidad = int(input("Cantidad: "))

# Crear diccionario y agregarlo a la lista
nuevo_producto = {
    "nombre": nuevo_nombre,
    "precio": nuevo_precio,
    "cantidad": nueva_cantidad
}
productos.append(nuevo_producto)

print("\n Producto agregado correctamente.")

# === GUARDAR PRODUCTOS ACTUALIZADOS ===
with open("productos.txt", "w") as archivo:  # "w" sobrescribe el contenido
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print(" Archivo 'productos.txt' actualizado con éxito.")
