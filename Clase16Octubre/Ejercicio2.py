import os

def count_lines_and_words(path):
     if not os.path.exists(path):
         raise FileNotFoundError("El archivo no existe")

     with open(path, 'r') as file:
         lines = file.readlines()
         if len(lines) == 0:
             raise ValueError("El archivo esta vacio")
         words = 0
         for line in lines: #Recorre cada línea del archivo
             words += len(line.split()) #line.split() divide la línea en palabras usando espacios como separador / len(line.split()) devuelve el número de palabras en esa línea
         return len(lines), words

     # 💡 Ejemplo:
     # line = "Python es genial"
     # line.split() → ["Python", "es", "genial"]
     # len(line.split()) → 3

try:
    lines, words = count_lines_and_words("ejemplo.txt") #llama a la función y desempaqueta la tupla en dos variables
    print(f"El numero de lineas del archivo ejemplo.txt es {lines} y el de palabras es {words}")
except Exception as e:
    print(e)