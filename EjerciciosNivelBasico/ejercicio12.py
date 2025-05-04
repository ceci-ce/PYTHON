"""Ejercicio 12¶
Escribe un programa que pida al usuario dos números enteros e imprima la secuencia de números entre ellos (incluidos)
en orden ascendente. Si el primer número es mayor que el segundo, imprime la secuencia en orden descendente. Debes
imprimir la secuencia de números en una sola línea, separados por espacios.

"""
numero_3 = int(input("Dime el primer numero: "))
numero_4 = int(input("Dime el segundo numero: "))

if numero_3 < numero_4:
    for i in range (numero_3,numero_4 + 1):
        print (i, end=" ")
elif numero_3 > numero_4:
    for i in range (numero_3,numero_4 - 1, - 1):
        print (i, end=" ")