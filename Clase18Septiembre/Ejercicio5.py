# Eliminar duplicados

lista = input("Introduce una lista de palabras separadas por comas\n")
lista_separada = lista.split(", ")
lista_sin_duplicados = set(lista_separada)

print(sorted(lista_sin_duplicados))