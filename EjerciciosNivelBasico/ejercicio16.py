"""Ejercicio 16¶
Escribe un programa que pida al usuario un número entero positivo e imprima la lista de divisores de ese número.
Un divisor de un número n es un número entero que divide a n sin dejar residuo. El programa debe imprimir todos los
 divisores del número introducido.

"""

numero_8 = int(input("Dime un numero entero: "))

print(f"Los divisores de {numero_8} son: ", end=" ")
for i in range(1,numero_8 + 1):
    if numero_8 % i == 0:
        print(i, end=" ")
print()