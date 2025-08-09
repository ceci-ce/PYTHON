"""Ejercicio 5 - Biblioteca digital¶
Escribe un programa que gestione una biblioteca digital utilizando un diccionario. El programa debe permitir al usuario
añadir libros con su título, autor y año de publicación. El usuario debe poder consultar los libros por autor o por año
de publicación. El programa debe ejecutarse indefinidamente hasta que el usuario introduzca "SALIR"."""

biblioteca_digital = {}
opcion = -1

while opcion != 4:
    print("Elige una opcion: ")
    print("1.Añadir libro")
    print("2.Consultar libro por autor")
    print("3.Consultar libro por año de publicacion")
    print("4.Salir")

    opcion = int(input("Introduce una opcion: ").strip())

    if opcion == 1:
        titulo = input("Escribe el titulo: ").strip()
        autor = input("Escribe el autor: ").strip()
        año = input("Escribe el año: ").strip()

        biblioteca_digital[titulo] = {"autor": autor, "año": año}
        print(f"El autor del libro {titulo} es {autor} y es del año {año}")
    elif opcion == 2:
        autor_buscar = input("Introduce el autor a buscar: ").strip().lower()

        # lista vacia para guardar coincidencias
        encontrados = []

        # recorremos todo el diccionario (recorrer claves y valores)
        for titulo, datos in biblioteca_digital.items():
            autor_guardado = datos["autor"].lower() # significa: Del diccionario datos, dame el valor que está en la clave 'autor'
            if autor_guardado == autor_buscar:
                encontrados.append(titulo)

        # Mostramos resultados
        if encontrados:
            print(f"Libros de {autor_buscar.title()}: ")
            for libro in encontrados:
                print(f"- {libro}({biblioteca_digital[libro]['año']})")
        else:
            print("No se encontraron libros de este autor.")


    elif opcion == 3:
        año_buscar = input("Introduce el año: ").strip()
        encontrados = []

        for titulo, datos in biblioteca_digital.items():
            if datos["año"] == año_buscar:
                encontrados.append(titulo)

        if encontrados:
            print(f"Libros publicados en: {año_buscar}")
            for libro in encontrados:
                print(f"{- libro}({biblioteca_digital[libro]['autor']})")
        else:
            print("No se encontraron libros de este año.")

    elif opcion == 4:
        print("Saliendo del programa...")

    else:
        print("Opción no válida.")

