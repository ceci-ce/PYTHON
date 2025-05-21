#Ejercicio 9 - Suma acumulativa¶
#Escribe un programa que pida al usuario una serie de números enteros y calcule la suma acumulativa de esos números.
#El programa debe seguir pidiendo números hasta que el usuario ingrese un 0. Al final, imprime la suma total.

numeros_enteros = int(input("Dime una serie de numeros enteros: "))
resultado = 0

while numeros_enteros != 0:
    resultado = numeros_enteros + resultado
    numeros_enteros = int(input())

print(f"El resultado es {resultado}")
