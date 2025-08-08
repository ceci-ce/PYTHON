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

    if opcion == 1:
        titulo = input("Escribe el titulo: ")
        autor = input("Escribe el autor: ")
        año = input("Escribe el año: ")

        biblioteca_digital[titulo] = {"autor": autor, "año": año}
        print(f"El autor del libro {titulo} es {autor} y es del año {año}")