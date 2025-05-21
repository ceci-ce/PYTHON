"""Ejercicio 18¶
Escribe un programa que dado una serie de números introducidos por el usuario, hasta que introduzca un -1, imprima el
número introducido sumándole 1. El programa debe imprimir todos los números introducidos, menos el -1, sumándoles 1."""

while True:
    numero = int(input("Introduce un número (-1 para salir): "))
    if numero == -1:
        break
    print(numero + 1)
