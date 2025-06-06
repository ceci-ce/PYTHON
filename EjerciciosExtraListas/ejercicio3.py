"""Ejercicio 3 - Filtrar elementos de una lista¶
Escribe un programa que pida al usuario una lista de números enteros separados por comas y filtre los números pares de
la lista. El programa debe imprimir la lista de números pares."""

numeros = input("Ingrese una lista de números enteros separados por comas: ").split(",")
numeros = [int(num) for num in numeros]
numeros_pares = []

for num in numeros:
    if num % 2 == 0:
        numeros_pares.append(num)
print(f"La lista de numeros pares es: ", numeros_pares)
