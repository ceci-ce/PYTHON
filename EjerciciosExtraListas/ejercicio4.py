"""Ejercicio 4 - Sumar dos listas de diferente longitud¶
Escribe un programa que pida al usuario dos listas de números enteros separados por comas y sume los elementos de ambas
listas. Si las listas no tienen la misma longitud, el programa debe sumar los elementos de la lista más corta con los
elementos correspondientes de la lista más larga y el resto de los elementos de la lista más larga deben ser sumados a
cero. El programa debe imprimir la lista resultante."""

lista1 = input("Ingrese la primera lista de números enteros separados por comas: ").split(",")
lista2 = input("Ingrese la segunda lista de números enteros separados por comas: ").split(",")
lista1 = [int(num) for num in lista1]
lista2 = [int(num) for num in lista2]
longitud_maxima = max(len(lista1), len(lista2))
suma_listas = []

for i in range(longitud_maxima):
    num1 = lista1[i] if i < len(lista1) else 0
    num2 = lista2[i] if i < len(lista2) else 0
    suma_listas.append(num1 + num2)

print("Lista resultante:", suma_listas)
