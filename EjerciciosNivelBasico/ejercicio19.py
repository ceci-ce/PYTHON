"""Ejercicio 19¶
Escribe un programa que dado una serie de notas introducidas por el usuario, hasta que introduzca un -1, imprima el
número de notas correctas introducidas, la media de las notas y cuantas de estas notas son 10. El programa debe imprimir
 la media de todas las notas introducidas, menos el -1."""

suma_notas = 0
contador_notas = 0
contador_diez = 0


while True:
    nota = float(input("Introduce la  siguiente nota: "))
    if nota == -1:
        break
    if 0 <= nota <= 10:
        suma_notas += nota
        contador_notas += 1
        if nota == 10:
            contador_diez += 1

if contador_notas > 0:
    media = suma_notas/contador_notas
    print(f"Numero de notas correctas: {contador_notas}")
    print(f"Media de notas: {media}")
    print(f"Numero de dieces: {contador_diez}")
else:
    print("Introduce una nota valida")

