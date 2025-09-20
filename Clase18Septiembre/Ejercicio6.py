palabras_feas = ["perro", "queso", "examen"]
frase = input("Dime una frase:\n")
"""
for palabra in palabras_feas:
    frase = frase.replace(palabra, "*"*len(palabra))

print(frase)
"""

# OPCION 2
frase_separada = frase.split()
nueva_frase = []
for palabra in frase_separada:
    if palabra in palabras_feas:
        palabra = "*"*len(palabra)
    nueva_frase.append(palabra)
print(" ".join(nueva_frase))

