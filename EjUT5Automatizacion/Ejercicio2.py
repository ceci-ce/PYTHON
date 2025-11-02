# Ejercicio 2 - Crear un directorio¶
# Escribe un script que reciba como argumento el nombre de un nuevo directorio y lo cree en el sistema de archivos.

import os


def make_directory(path): #recibe como argumento la ruta del directorio a crear (path)
    path_splitted = path.split("/") #Divide la ruta que introdujo el usuario en partes, separadas por las barras /
    for i in range(len(path_splitted)):
        if i == len(path_splitted) - 1 and os.path.exists(path_splitted[i]): #Comprueba si la última carpeta (la final del camino) ya existe.
            raise FileExistsError("El directorio ya existe") #Si existe, lanza un error FileExistsError para avisar que no hace falta crearla

        if not os.path.exists(path_splitted[i]): #Si la carpeta actual no existe, la crea con os.mkdir()
            os.mkdir(path_splitted[i])
        os.chdir(path_splitted[i]) #Cambia el directorio de trabajo a la carpeta recién creada o ya existente, usando os.chdir().
                                #Esto es importante porque en la siguiente iteración se creará la siguiente carpeta dentro de la anterior.


path = input("Introduce el nombre del nuevo directorio que quieres crear\n")

try:
    make_directory(path)
except Exception as e:
    print(e)