import os


def list_directory(path): #Se define una función que recibe un parámetro path, que será la ruta del directorio a listar.
    if not os.path.exists(path):
        raise FileNotFoundError("No existe el directorio especificado")

    elementos = os.listdir(path) #para obtener una lista de nombres de todo lo que hay dentro del directorio
    resultado = { #Crea un diccionario para guardar los resultados por separado
        "archivos": [],
        "directorios": []
    }
    for elem in elementos:
        if os.path.isfile(elem): #Si el elemento es un archivo → se añade a la lista "archivos"
            resultado["archivos"].append(elem)
        elif os.path.isdir(elem): #Si es un directorio → se añade a "directorios"
            resultado["directorios"].append(elem)

    return resultado #Devuelve el diccionario con la información recopilada


path = input("Introduce la ruta que quieres listar\n")

try:
    print(list_directory(path)) #Llama a la función con la ruta introducida
except Exception as e: #Si ocurre un error (por ejemplo, el directorio no existe), se captura y muestra el mensaje
    print(e)