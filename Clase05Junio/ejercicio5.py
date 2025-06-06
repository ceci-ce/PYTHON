"""Ejercicio 5 - Calcular la suma de dígitos de un número¶
Escribe un programa que pida al usuario un número entero y calcule la suma de sus dígitos. El programa debe definir una
función que reciba el número, realice el cálculo de la suma de los dígitos y luego imprima el resultado.

"""

def suma_digitos(numero):
    resultado = 0
    while numero > 0:
        resultado += numero%10 # Obtiene el último dígito del número.
        numero //= 10 #Elimina el último dígito (división entera entre 10).
    return resultado

numero = int(input("Introduce un numero entero positivo: "))
print(f"La suma de los digitos de {numero} es {suma_digitos(numero)}")

""" EJEMPLO:

Entonces:

472 % 10 = 2

472 // 10 = 47

47 % 10 = 7

47 // 10 = 4

4 % 10 = 4

4 // 10 = 0

Suma total: 2 + 7 + 4 = 13


"""