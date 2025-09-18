# Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range
multiplos_de_4=list(range(4, 101, 4))
print(multiplos_de_4)
# Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
elementos=["manzana,banana,naranja,uva,pera"]
print(elementos[-2])
#Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo:
lista_vacia=[]
lista_vacia.append("lechuga,tomate,cebolla")
# Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! 
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)
#Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
print("el ejercicio 5 imprime la lista,removiendo el numero maximo de la lista")
#Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
numeros = list(range(10, 31, 5))
print(numeros[:2])
#  Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores 
cualesquiera. 
autos = ["sedan", "polo", "suran", "gol"] 
autos[1,2]="gol, ranger"
print("autos")
#Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla. 
dobles=[]
dobles.appened(2*5)
dobles.append(2*10)
dobles.append(2*15)
print(dobles)
#Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes: 
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], 
["agua"]]
#Agregar producto
compras[2].append("jugo")
#Reemplazar producto
compras[1][2]="tallarines"
#Eliminar producto
compras[0][0].remove("pan")
print(compras)
#Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
lista_anidada = [[15], [False, True], [25.5, 57.9, 30.6], [False]]
print(lista_anidada)