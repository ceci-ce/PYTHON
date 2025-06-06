"""Ejercicio 2 - Multiplicar todos los elementos de una lista¶
Escribe un programa que pida al usuario una lista de números enteros separados por espacios y un número entero.
El programa debe multiplicar todos los elementos de la lista por el número dado y luego imprimir la lista resultante."""

numeros = input("Ingrese una lista de números enteros separados por espacios: ").split()
numeros = [int(num) for num in numeros]
numero_a_multiplicar = int(input("Ingrese un número entero: "))
for i in range(len(numeros)):
    numeros[i] *= numero_a_multiplicar
print("Lista resultante:", numeros)
