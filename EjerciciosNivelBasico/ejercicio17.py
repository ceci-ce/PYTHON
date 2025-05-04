"""Ejercicio 17¶
Escribe un programa que reciba un número entero positivo y una letra. El programa debe imprimir la letra tantas veces
como el número introducido."""

numero_9 = int(input("Dime un numero entero: "))
letra = input("Dime una letra: ")

for i in range (1,numero_9 + 1):
    print(letra, end=" ")
