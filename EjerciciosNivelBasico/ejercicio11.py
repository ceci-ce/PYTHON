"""Ejercicio 11¶
Escribe un programa que pida al usuario dos números enteros e imprima la secuencia de números entre ellos (incluidos)
en orden ascendente. El primer número siempre será menor que el segundo."""

numero_1 = int(input("Dime el primer numero: "))
numero_2 = int(input("Dime el segundo numero: "))

for i in range (numero_1,numero_2,1):
    print(i + 1)