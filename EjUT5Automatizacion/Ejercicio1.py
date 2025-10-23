# Ejercicio 1 - Listar archivos en un directorio¶
# Escribe un script que reciba como argumento el nombre de un directorio y liste todos los archivos y subdirectorios que contiene.

import os
import sys

# Comprobamos que se haya pasado un argumento, Queremos asegurarnos de que el usuario haya pasado al menos un argumento además del nombre del script.
# sys.argv == ['listar_archivos.py', 'C:\\Users\\Cecilia\\Documents']

if len(sys.argv) < 2:
    print("Uso: python listar_archivos.py <nombre_directorio>")
    sys.exit(1) # se usa para errores de uso o validación inicial

# Guardamos el argumento (la ruta del directorio)

directorio = sys.argv[1]

# Verificamos que el directorio exista

if not os.path.exists(directorio):
    print("El directorio no existe")
    sys.exit(1)

# Listamos todos los elementos del directorio

print(f"Contenido del directorio '{directorio}':\n")

for elemento in os.listdir(directorio): #os.listdir(path) devuelve una lista de nombres (strings) con todo lo que hay dentro del directorio path
    ruta_completa = os.path.join(directorio, elemento) #os.path.join() combina varias partes de una ruta (por ejemplo, una carpeta y un nombre de archivo) en una sola cadena de texto, usando el separador correcto según el sistema operativo.
    if os.path.isdir(ruta_completa):
        print(f"[DIR]  {elemento}")  # es una carpeta
    else:
        print(f"[FILE] {elemento}")  # es un archivo