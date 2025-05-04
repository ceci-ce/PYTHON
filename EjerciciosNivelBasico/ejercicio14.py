"""Ejercicio 14¶
Escribe un programa que pida al usuario un número entero positivo e imprima la suma de los números pares por un lado
y la suma de los números impares por otro. El programa debe imprimir ambos resultados."""

numero_6 = int(input("Dime un numero entero: "))

suma_pares = 0 # se inician las variables de suma en cero, antes de empezar a acumular valores en el bucle
suma_impares = 0

for i in range(1, numero_6 + 1):
    if i % 2 == 0:
        suma_pares += i # es lo mismo que: suma_pares = suma_pares + i
    else:
        suma_impares += i

print(f"Suma de numeros pares: {suma_pares}")
print(f"Suma de numeros impares: {suma_impares}")



