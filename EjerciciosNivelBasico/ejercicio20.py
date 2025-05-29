"""Ejercicio 20¶
Escribe un programa que dado una serie de números introducidos por el usuario, hasta que introduzca un -1, cuente cuántos
 de estos números son pares y cuántos son impares. El programa debe imprimir el número de pares e impares introducidos,
 menos el -1."""

contador_pares = 0
contador_impares = 0

while True:
    numero = int(input("Introduce un numero: "))
    if numero == -1:
        break
    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1

print(f"Número de pares: {contador_pares}")
print(f"Número de impares: {contador_impares}")

