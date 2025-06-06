"""Ejercicio 1 - Contar la frecuencia de un número en una lista¶
Escribe un programa que pida al usuario una lista de números enteros separados por espacios y un número entero. El
programa debe contar cuántas veces aparece el número en la lista y luego imprimir el resultado."""

numeros = input("Ingresa una lista de numeros enteros separados por espacios: ").split() #Se pide una lista de strings y se separan por espacios
numeros = [int(num) for num in numeros] #Convierte cada elemento de la lista (que son strings) en un número entero.
numero_a_contar = int(input("Ingresa un numero entero: "))
frecuencia = numeros.count(numero_a_contar)
print(f"El numero {numero_a_contar} aparece {frecuencia} veces en la lista")
