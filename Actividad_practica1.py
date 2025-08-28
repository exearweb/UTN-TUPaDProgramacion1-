#Ejercicio 1
ancho=int(input ("escriba el ancho del rectangulo"))
alto=int(input("Escriba el alto del rectangulo"))
area=(ancho*alto)
perimetro=(ancho*2)+(ancho*2)
print(f"el area del rectangulo es {area} ,y su perimetro es, {perimetro}")
#Ejercicio 2
c=float(input("ingrese grados celsius"))
f=round(c*9/5)+32
print(f"la cantidad de {c}son equivalentes a {f} grados farenheit")
#Ejercicio 3
a=True
b=False
#a and b
print("a and b",a and b)
print("a or b", a or b)
print(not a,not b)
#Ejercicio 4
a=5
b=3
a=2
c=a+b
print(c)
#Ejercicio 5
numero=int(input("escribe un numero"))
cuadrado_numero=input(numero**2)
print("el cuadro del numero es {cuadrado_numero}")
#Ejercicio 6: Intercambio de variables
x= 10
y= 20
c= y/x
print(c)
#Ejercicio 7
peso = float(input("Ingrese su peso en kg "))
altura = float(input("Ingrese su altura en metros"))

imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc}")

#Ejercicio 9
a = 7.5
b = 3.2

# Suma
suma = a + b
print("La suma es:", suma)

# División con redondeo a 2 decimales
division_redondeada = round(a / b, 2)
print("La división redondeada a 2 decimales es:", division_redondeada)

# Potencia
potencia = a ** b
print("La potencia (a ** b) es:", potencia)

#Ejercicio 10
precio_original = float(input("precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))


precio_final = precio_original * (1 - (descuento / 100))


print("El precio final con descuento es:", precio_final)
