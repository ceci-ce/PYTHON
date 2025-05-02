"""Ejercicio 8¶
Escribe un programa que pida el nombre de un mes y muestre cuántos días tiene (puedes simplificar febrero a 28 días
siempre)."""

mes = input("Dime un mes: ").lower()

if mes in ["enero", "marzo","mayo","julio","agosto","octubre","diciembre"]:
    print(f"El mes {mes.capitalize()} tiene 31 dias")
elif mes in ["abril","junio","septiembre","noviembre"]:
    print(f"El mes {mes.capitalize()} tiene 30 dias")
elif mes == "febrero":
    print(f"El mes {mes.capitalize()} tiene 28 dias")
else:
    print("No es un mes valido")