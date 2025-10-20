# Creamos el diccionado proporcionado en el enunciado
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Imprimimos el diccionario original
print(precios_frutas)

# Agregamos, una a una, las frutas nuevas
# Como estas keys no existen en el diccionario, se añadirán
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

# Imprimimos la nueva versión del diccionario
print(precios_frutas)

# Modificamos, uno a uno, los precios de las frutas
# Como estas keys ya existen en el diccionario, se modificarán
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

# Imprimimos la nueva versión del diccionario
print(precios_frutas)

# Las frutas son las keys del diccionario, por lo que podemos obtenerlas con el método .keys()
frutas = precios_frutas.keys()

# Imprimimos el resultado
print(frutas)

# Como vemos, la estructura obtenida no es una lista nativa de Python
# Sin embargo, podemos convertirla a lista usando la función list()

frutas = list(frutas)

print(frutas)

contactos = {}

for _ in range(5):
    nombre = input("Ingresá el nombre del contacto: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    contactos[nombre] = numero

consulta = input("Ingresá el nombre del contacto a consultar: ")

if consulta in contactos:
    print(f"El número de {consulta} es {contactos[consulta]}")
else:
    print("Contacto no encontrado.")

frase = input("Ingresá una frase: ")
palabras = frase.split()

unicas = set(palabras)
print("Palabras únicas:", unicas)

recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("Recuento:", recuento)

alumnos = {}

for _ in range(3):
    nombre = input("Nombre del alumno: ")
    notas = []
    for i in range(3):
        nota = float(input(f"Ingresá la nota {i+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno} tiene un promedio de {promedio:.2f}")

parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7, 8}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

productos = {
    "manzanas": 10,
    "bananas": 5,
    "naranjas": 8
}

producto = input("Ingresá el nombre del producto: ")

if producto in productos:
    agregar = int(input("¿Cuántas unidades querés agregar?: "))
    productos[producto] += agregar
    print(f"Nuevo stock de {producto}: {productos[producto]}")
else:
    nuevo_stock = int(input("Producto nuevo. Ingresá el stock inicial: "))
    productos[producto] = nuevo_stock
    print(f"Producto {producto} agregado con {nuevo_stock} unidades.")
#Ejercicio 9
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("viernes", "18:00"): "Gimnasio"
}

dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (ej: 10:00): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad: {agenda[clave]}")
else:
    print("No hay actividades programadas.")
#Ejercicio 10
paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia"
}

invertido = {}

for pais, capital in paises.items():
    invertido[capital] = pais

print("Diccionario original:", paises)
print("Diccionario invertido:", invertido)
