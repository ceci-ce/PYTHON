import os

# Ejercicio 5 - Censurar palabras en un archivo¶
# Escribe un programa que abra un archivo de texto y reemplace todas las ocurrencias de una palabra específica por otra
# palabra. El programa debe definir una función que reciba el nombre del archivo, la palabra a censurar y la palabra de
# reemplazo, y luego realice la censura en el archivo.

def replace_word(path, word_to_replace, new_word):
    if not os.path.exists(path):
        raise FileNotFoundError(f"El archivo {path} no existe")
    if len(word_to_replace) == 0:
        raise ValueError("La palabra a remplazar no puede ser vacía")

    with open(path, 'r') as file:
        text = file.read()
        text = text.replace(word_to_replace, new_word)

    with open(path, 'w') as file:
        file.write(text)

path = input("Qué archivo quieres censurar? \n")
word_to_replace = input("Qué palabra quieres censuarar? \n")
new_word = input("Por que palabra quieres sustituirla? \n")

try:
    replace_word(path, word_to_replace, new_word)
except Exception as e:
    print(e)