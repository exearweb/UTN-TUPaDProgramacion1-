#Ejercicio 1
edad=int(input ("ingrese su edad"))
if(edad>18):
    print("Es mayor de edad")
#Ejercicio 2
nota= int(input ("ingrese su nota"))
if(nota>6):
    print("Aprobado")
elif(nota<6):
    print("Desaprobado")
#Ejercicio 3
numero=int(input("Ingrese un numero"))
if(numero % 2 ==0):
    print("numero par")
else:
    print("es impar")
print("hola")
numero1=int(input("ingrese un numero"))
if(numero1 % 2 !=0):
    print("es impar")

    #Ejercio 4 Niño/a: menor de 12 años.Adolescente: mayor o igual que 12 años y menor que 18 años.Adulto/a joven: mayor o igual que 18 años y menor que 30 años.Adulto/a: mayor o igual que 30 años
edad=int(input("Ingrese su edad"))
if(edad<12):
    print("Niño")
elif(edad>=12 and edad<18):
    print("Adolescente")
elif(edad>=18):
    print("adulto joven")
else:
    print("adulto mayor")
#Ejercicio 5
# Programa para validar contraseña según su longitud

# Solicitar la contraseña al usuario
contraseña = input("Ingrese una contraseña: ")

# Verificar la longitud usando len()
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    #Ejercicio 6
    #Importamos todos los paquetes y funciones que necesitamos utilizar
    
    import random
    from statistics import mode, median, mean
    #Generamos una lista de 50 numeros de forma aleatoria
    numeros_aleatorios = [random.raint(1, 100)for i in range(50)]
    #Calculamos la moda, la mediana y la media de la lista numeros_aleatorios
    moda= mode(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    media = mean(numeros_aleatorios)
    
    #Si la media es mayor que la mediana y la mediana es mayor que la moda, imprimir "sesgo positivo o la derecha"
    if media>mediana>moda: 
        print("Sesgo positivo o a la derecha")
    #Si la media es menor que la mediana  la mediana es menor que la moda, impirmir "sesgo negativo o a la izquierda"
    elif media<mediana<moda:
        print("sesgo negativo o a la izquierda")
    #Si la media, la mediana y la moda son iguales, imprimir "sin sesgo"
    elif media == mediana ==moda:
        print("sin sesgo")
    #Si no se cumple ninguna de las condiciones anteriores, imprimir "No se puede determinar si esta distribucion tiene sesgo o no"
    else:
        print("No se puede determinar si esta distribucion tiene sesgo o no")

    #Ejercicio 7
    #Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
    # Solicitar una frase o palabra al usuario
    texto = input("Ingrese una frase o palabra: ")

    # Verificar si termina con una vocal (mayúscula o minúscula)
    if texto and texto[-1].lower() in "aeiou":
        texto += "!"
    print(texto)

#Ejercicio 8
nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese 1 para mayúsculas, 2 para minúsculas, 3 para primera letra mayúscula: ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.capitalize())
else:
    print("Opción no válida")
#Ejercicio 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")
    
#Ejercicio 10
hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").strip().upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

# Convertir mes y día a un número para comparar fácilmente (MMDD)
fecha = mes * 100 + dia

if hemisferio == "N":
    if 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
        estacion = "Invierno"
    elif 321 <= fecha <= 620:
        estacion = "Primavera"
    elif 621 <= fecha <= 920:
        estacion = "Verano"
    elif 921 <= fecha <= 1220:
        estacion = "Otoño"
    else:
        estacion = "Fecha inválida"
elif hemisferio == "S":
    if 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
        estacion = "Verano"
    elif 321 <= fecha <= 620:
        estacion = "Otoño"
    elif 621 <= fecha <= 920:
        estacion = "Invierno"
    elif 921 <= fecha <= 1220:
        estacion = "Primavera"
    else:
        estacion = "Fecha inválida"
else:
    estacion = "Hemisferio no válido"

print("La estación es:", estacion)
