"""Ejercicio 5¶
Escribe un programa que pida el nombre de un día de la semana y muestre si es "laborable" o "fin de semana".
"""

"""dia = input("Dime un dia de la semana: ")

if dia == "lunes" or dia == "martes" or dia ==  "miercoles" or dia ==  "jueves" or dia == "viernes":
    print ("Es un dia laborable")
else:
    print("Es fin de semana")
    """

dia = input("Dime un dia de la semana: ").lower()

if dia in ["lunes","martes","miercoles","jueves","viernes"]:
    print(f"{dia.capitalize()} es laborable")
elif dia in ["sabado", "domingo"]:
    print(f"{dia.capitalize()} es fin de semana")
else:
    print("No es un dia valido")



