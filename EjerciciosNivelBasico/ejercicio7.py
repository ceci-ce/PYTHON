"""Ejercicio 7¶
Escribe un programa que pida dos números y un operador (+, -, *, /) y muestre el resultado de la operación.
"""


num1 = int(input("Numero uno: "))
num2 = int(input("Numero dos: "))
operador = input("Introduce un operador (+, -, *, /): ")

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1*num2
elif operador == "/":
    if num2 != 0:
        resultado = num1/num2
    else:
        resultado = "Error: division por cero"
else:
    resultado = "Operador no valido"
print(f"Resultado: {resultado}")



