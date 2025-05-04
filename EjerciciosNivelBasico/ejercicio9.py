"""Ejercicio 9¶
Escribe un programa que pida el precio de un producto y, si supera los 100€, aplique un descuento del 10%. Muestra
el precio final."""

precio = int(input("Dime el precio del producto: "))

if precio < 100:
    print(f"El precio del producto es {precio} €")
elif precio > 100:
    descuento = (precio - (precio * 0.10))
    print(f"El precio del producto es {descuento} €")
else:
    print("No es una opcion valida")