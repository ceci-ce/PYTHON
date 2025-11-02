#Ejercicio 3 - Eliminar un archivo¶
#Escribe un script que reciba como argumento el nombre de un archivo y lo elimine del sistema de archivos.

import os

def delete_file(path):
    if not os.path.exists(path):
        raise FileNotFoundError("El archivo no existe")

    if os.path.isdir(path):
        raise ValueError(f"{path} es un directorio")

    os.remove(path)
    return f"El archivo {path} ha sido eliminado con exito"

path = input("Introduce la ruta del fichero que quieres eliminar\n")

try:
    delete_file(path)
except Exception as e:
    print(e)


