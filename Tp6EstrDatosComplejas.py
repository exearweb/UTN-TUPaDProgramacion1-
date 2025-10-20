# Actividad 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Mostrar resultado
print("Actividad 1 - precios_frutas actualizado:")
print(precios_frutas)
# Actividad 2 (parteada sobre el diccionario resultado de la actividad 1)
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450,
                  'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

# Actualizaciones pedidas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Actividad 2 - precios actualizados:")
print(precios_frutas)
# Actividad 3
precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450,
                  'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

frutas = list(precios_frutas.keys())  # lista de claves
print("Actividad 3 - lista de frutas:")
print(frutas)
# Actividad 4
def cargar_contactos(n=5):
    agenda = {}
    for i in range(n):
        nombre = input(f"Ingrese nombre del contacto {i+1}: ").strip()
        numero = input(f"Ingrese número de {nombre}: ").strip()
        agenda[nombre] = numero
    return agenda

def consultar_contacto(agenda):
    nombre = input("Ingrese el nombre a consultar: ").strip()
    if nombre in agenda:
        print(f"Número de {nombre}: {agenda[nombre]}")
    else:
        print(f"{nombre} no está en la agenda.")

# Ejecución ejemplo
if __name__ == "__main__":
    print("Cargando 5 contactos:")
    agenda = cargar_contactos(5)
    print("\nConsulta:")
    consultar_contacto(agenda)
# Actividad 5
frase = input("Ingrese una frase: ").strip()

# Normalizamos: pasamos a minúsculas y separamos por espacios
palabras = frase.lower().split()

# set de palabras únicas
unicas = set(palabras)

# diccionario con conteo de cada palabra
conteo = {}
for p in palabras:
    conteo[p] = conteo.get(p, 0) + 1

print("Palabras únicas:", unicas)
print("Conteo por palabra:", conteo)
# Actividad 6
def cargar_alumnos(n=3):
    alumnos = {}
    for i in range(n):
        nombre = input(f"Ingrese nombre del alumno {i+1}: ").strip()
        notas = []
        for j in range(3):
            while True:
                try:
                    nota = float(input(f"  Ingrese nota {j+1} de {nombre}: "))
                    notas.append(nota)
                    break
                except ValueError:
                    print("  Valor no valido. Ingrese un número.")
        alumnos[nombre] = tuple(notas)
    return alumnos

def promedios(alumnos):
    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"{nombre}: notas={notas} -> promedio={promedio:.2f}")

if __name__ == "__main__":
    alumnos = cargar_alumnos(3)
    promedios(alumnos)
# Actividad 7
parcial1 = set(input("Ingrese alumnos aprobados en Parcial 1 (separados por coma): ").split(","))
parcial2 = set(input("Ingrese alumnos aprobados en Parcial 2 (separados por coma): ").split(","))

# Limpiar espacios
parcial1 = {a.strip() for a in parcial1 if a.strip()}
parcial2 = {a.strip() for a in parcial2 if a.strip()}

ambos = parcial1 & parcial2  # intersección
solo_uno = parcial1 ^ parcial2  # elementos que están en uno u otro pero no en ambos (xor simétrico)
al_menos_uno = parcial1 | parcial2  # unión

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)
# Actividad 8
stock = {}  # {'producto': cantidad}

def consultar_stock(producto):
    cantidad = stock.get(producto)
    if cantidad is None:
        print(f"{producto} no existe en el stock.")
    else:
        print(f"Stock de {producto}: {cantidad}")

def agregar_unidades(producto, unidades):
    if producto in stock:
        stock[producto] += unidades
        print(f"Se agregaron {unidades} unidades a {producto}. Nuevo stock: {stock[producto]}")
    else:
        print(f"{producto} no existe. Use 'agregar_producto' para crearlo.")

def agregar_producto(producto, unidades):
    if producto in stock:
        print(f"{producto} ya existe. Use agregar_unidades.")
    else:
        stock[producto] = unidades
        print(f"Producto {producto} creado con stock {unidades}.")

# Ejemplo de uso interactivo
if __name__ == "__main__":
    while True:
        print("\nOpciones: 1)consultar 2)agregar_unidades 3)agregar_producto 4)mostrar 5)salir")
        opcion = input("Seleccione opción: ").strip()
        if opcion == "1":
            p = input("Producto a consultar: ").strip()
            consultar_stock(p)
        elif opcion == "2":
            p = input("Producto: ").strip()
            u = int(input("Unidades a agregar: "))
            agregar_unidades(p, u)
        elif opcion == "3":
            p = input("Nuevo producto: ").strip()
            u = int(input("Unidades iniciales: "))
            agregar_producto(p, u)
        elif opcion == "4":
            print("Stock actual:", stock)
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")
# Actividad 9
agenda = {}  # clave: (dia, hora) -> valor: evento

def agregar_evento(dia, hora, evento):
    clave = (dia, hora)
    agenda[clave] = evento
    print(f"Agregado: {clave} -> {evento}")

def consultar_evento(dia, hora):
    clave = (dia, hora)
    evento = agenda.get(clave)
    if evento:
        print(f"En {dia} a las {hora} hay: {evento}")
    else:
        print(f"No hay actividad registrada para {dia} a las {hora}.")

# Ejemplo
if __name__ == "__main__":
    agregar_evento("Lunes", "19:00", "Clase de fútbol")
    agregar_evento("Jueves", "19:00", "Entrenamiento")
    consultar_evento("Lunes", "19:00")
    consultar_evento("Martes", "10:00")
# Actividad 10
paises_a_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasília',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo'
}

# Construir diccionario invertido: capital -> pais
capital_a_pais = {capital: pais for pais, capital in paises_a_capitales.items()}

print("Diccionario original (pais->capital):")
print(paises_a_capitales)
print("Diccionario invertido (capital->pais):")
print(capital_a_pais)
