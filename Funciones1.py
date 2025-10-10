#Función imprimir_hola_mundo()
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Programa principal
imprimir_hola_mundo()

#Función saludar_usuario(nombre)
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Programa principal
nombre = input("Ingresa tu nombre: ")
print(saludar_usuario(nombre))

 #Función informacion_personal(nombre, apellido, edad, residencia)
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa principal
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

 #Funciones calcular_area_circulo() y calcular_perimetro_circulo()
import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa principal
radio = float(input("Ingresa el radio del círculo: "))
print("Área del círculo:", calcular_area_circulo(radio))
print("Perímetro del círculo:", calcular_perimetro_circulo(radio))

 #Función segundos_a_horas(segundos)
def segundos_a_horas(segundos):
    return segundos / 3600

# Programa principal
segundos = int(input("Ingresa la cantidad de segundos: "))
print("Equivale a", segundos_a_horas(segundos), "horas.")

#Función tabla_multiplicar(numero)
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Programa principal
num = int(input("Ingresa un número para ver su tabla de multiplicar: "))
tabla_multiplicar(num)

#Función operaciones_basicas(a, b)
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

# Programa principal
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

#Función calcular_imc(peso, altura)
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Programa principal
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")

#Función celsius_a_fahrenheit(celsius)
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Programa principal
celsius = float(input("Ingresa la temperatura en °C: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivalen a {fahrenheit}°F")

 #Función calcular_promedio(a, b, c)
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))

print("El promedio es:", calcular_promedio(a, b, c))