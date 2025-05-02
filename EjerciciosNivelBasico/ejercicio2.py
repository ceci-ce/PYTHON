#Ejercicio 2¶
#Escribe un programa que pida al usuario un número entero y determine si es positivo, negativo o cero. El programa debe
#imprimir un mensaje indicando el resultado.

num = int(input("Dime un numero: "))

if num > 0:
    print(f"El numero {num} es positivo")
elif num < 0:
    print(f"El numero {num} es negativo")
else:
    print("El numero es cero")

