"""Ejercicio 4 - Verificar si un número es primo¶
Escribe un programa que pida al usuario un número entero y verifique si es primo. El programa debe definir una función
que reciba el número, realice la verificación y luego imprima si el número es primo o no."""

"""un numero es primo si solo es divisible entre 1 y si mismo"""
def es_primo(numero):
    for i in range(2,numero): #saltamos el 1 xk entre 1 todos los numeros son divisibles
        if numero%i == 0:
            return False
    return True

numero = int(input())
print(es_primo(numero))
