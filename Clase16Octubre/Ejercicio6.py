# Ejercicio 6 - Buscar una palabra en un archivo¶
# Escribe un programa que abra un archivo de texto y busque todas las líneas que contienen una palabra específica. El
# programa debe definir una función que reciba el nombre del archivo y la palabra a buscar, y luego imprima todas las
# líneas que contienen esa palabra.

import os

def search_lines(path, word):
    if len(word) == 0:
        raise ValueError("La palabra no puede ser vacia")

    if not os.path.exists(path):
        raise FileNotFoundError(f"El archivo {path} no existe")

    with open(path, 'r') as file:
        for num, line in enumerate(file, start=1): #enumerate agrega un contador (num), que empieza en 1 gracias a start=1/Así puedes saber en qué número de línea estás
            if word in line:
                print(f"Linea {num}: {line}") #Comprueba si la palabra que buscas (word) está dentro de esa línea/Si la encuentra, entra al if

path = input("Que archivo quieres imprimir?\n")
word = input("Que palabra quieres buscar?\n")

try:
    search_lines(path, word)
except Exception as e:
    print(e)