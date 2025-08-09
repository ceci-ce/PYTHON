"""Ejercicio 7 - Búsqueda por valor en un diccionario¶
Escribe un programa que replique el comportamiento del ejercicio 1, pero en lugar de buscar por clave (país), el usuario
 debe poder buscar por valor (capital). El programa debe permitir al usuario introducir una capital y devolver el país
  correspondiente. Si la capital no está en el diccionario, el programa debe informar al usuario."""

paises = {}
entrada = input("Indica un valor de la forma Pais-Capìtal o escribe FIN INSERCIONES para finalizar: \n").lower()

while entrada != "FIN INSERCIONES".lower():
    # ["España", "Madrid"]
    pais = entrada.split("-")[0]
    capital = entrada.split("-")[1]
    paises [pais] = capital # Añade nuevo par clave-valor
    entrada = input("Indica un valor de la forma Pais-Capìtal o escribe FIN INSERCIONES para finalizar: \n").lower()

#print(paises)

capital_usuario = input("Introduce el nombre de la capital que quieres consultar: ").lower()

pais_encontrado = None
for pais, capital in paises.items():
    if capital.lower() == capital_usuario:
        pais_encontrado = pais
        break

if pais_encontrado:
    print(f"La capital {capital_usuario.capitalize()} pertenece al país {pais_encontrado.capitalize()}")
else:
    print("No existe ese registro en el diccionario")
