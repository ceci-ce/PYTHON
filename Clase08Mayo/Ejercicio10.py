"""Ejercicio 10 - Akinator numérico¶
Escribe un programa que escoja un número aleatorio entre 1 y 100 y le pida al usuario que adivine el número.
El programa debe dar pistas al usuario si el número es mayor o menor que el número elegido. El programa debe seguir
pidiendo números hasta que el usuario adivine el número correcto."""

import random

numero_usuario = int(input("Dime un numero aleatorio entre 1 y 100: "))
numero_aleatorio = random.randint(1,100)

while numero_usuario != numero_aleatorio:
    if numero_usuario < numero_aleatorio:
        print("Demasiado bajo")
    elif numero_usuario > numero_aleatorio:
        print("Demasiado alto")
    numero_usuario = int(input("Intentalo de nuevo: "))

print(f"Has encontrado el numero {numero_aleatorio}")

