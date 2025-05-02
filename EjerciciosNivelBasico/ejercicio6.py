"""Ejercicio 6¶
Escribe un porgrama que pida un año y muestra si es bisiesto. Un año es bisiesto si es divisible por 4, pero no por
100, o si es divisible por 400.
"""

año = int(input("Dime un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("Es bisiesto")
else:
    print("No es bisiesto")


