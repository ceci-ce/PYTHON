"""Ejercicio 12 - Mayor y menor¶
Escribe un programa que pida al usuario una serie de números enteros y determine cuál es el mayor y cuál es el menor.
El programa debe seguir pidiendo números hasta que el usuario ingrese un 0. Al final, imprime el mayor y el menor."""

mayor = float('-inf')
menor = float('inf')
numero = int(input("Introduce un valor (0 para terminar): "))

while numero != 0:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

    numero = int(input("Introduce un valor (0 para terminar): "))

print(f"Mayor: {mayor} Menor: {menor}")


"""EXPLICACION

se inicializan dos variables:

-mayor se inicia con el valor más bajo posible (-infinito) para que cualquier número ingresado lo supere.
-menor se inicia con el valor más alto posible (+infinito) para que cualquier número ingresado sea más pequeño.

Si el número actual es mayor que el guardado en mayor, lo actualiza.
Si el número actual es menor que el guardado en menor, lo actualiza también 
"""