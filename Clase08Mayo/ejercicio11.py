"""Ejercicio 11 - Media de notas¶
Escribe un programa que pida al usuario cuantas evaluaciones hay que cualificar. Seguidamente se recibirán ese número
de series de notas (números decimales entre 0 y 10) y calcule la media de esas notas. El programa debe seguir pidiendo
notas hasta que el usuario ingrese un -1. Al final, imprime la media."""

evaluaciones = int(input("Introduce el numero de evaluaciones: "))

for i in range(evaluaciones):
    nota = float(input("Introduce la  siguiente nota: "))
    num_notas = 0
    sum_notas = 0
    while nota != -1:
        num_notas += 1
        sum_notas += nota
        nota = float(input("Introduce la  siguiente nota: "))
    print(f"Nota media evaluacion {i + 1}: {sum_notas/num_notas}")
