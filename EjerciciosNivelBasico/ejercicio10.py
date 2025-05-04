"""Ejercicio 10¶
Escribe un programa que pida día, mes y año. Comprueba si la fecha introducida es válida. Recuerda que, en los años
bisiestos, febrero tiene 29 días. Puedes usar el algoritmo del ejercicio 6 para determinar si un año es bisiesto."""

dia = int(input("Introduce un dia: "))
mes = int(input("Introduce un mes del 1 al 12: "))
año = int(input("Introduce un año: "))

if mes < 1 or mes > 12:
    print("Mes no válido.")
elif (dia < 1 or (mes == 2 and ((año % 4 == 0 and año % 100 != 0) or (año % 400 == 0) and dia > 29)) or
      (mes == 2 and dia > 28) or (mes in [4, 6, 9, 11] and dia > 30) or (mes in [1, 3, 5, 7, 8, 10, 12] and dia > 31)):
    print("Fecha no válida.")
else:
    print(f"La fecha {dia}/{mes}/{año} es válida.")
