#Ejercicio 2 - Contador de números pares¶
#Escribe un programa que pida al usuario un número entero positivo y cuente cuántos números pares hay desde 0 hasta ese
#número (incluido). El programa debe imprimir el resultado.

# Recibo el número del usuario
numero = int(input("Introduce un numero entero positivo: "))

# Inicio una variable para ir contando los pares que hay en esa secuencia de numeros
pares = 0
# Para i en la secuencia [0,1,2,3,4...numero+1]
for i in range(0,numero+1):
    if i % 2 == 0: # miro si i es par
        pares = pares + 1  #Sumo 1 al contador de pares

print(f"Numero de pares: {pares}")


