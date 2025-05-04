"""Ejercicio 15¶
Escribe un programa que pida al usuario un número entero positivo y calcules la suma de la potencia de 3 de cada número
desde 1 hasta el número introducido. El programa debe imprimir el resultado."""

numero_7 = int(input("Dime un numero entero: "))
suma = 0

for i in range (1,numero_7 + 1):
    suma += i ** 3 # suma = suma + (i**3)

print (f"La suma de la potencia de 3 de los numeros desde 1 hasta {numero_7} es: {suma}" )