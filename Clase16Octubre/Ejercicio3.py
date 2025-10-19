# Definimos una función que recibe una lista de nombres y el nombre del archivo donde guardarlos
def escribir_nombres_en_archivo(nombres, archivo): #El tipo de cada parámetro dependerá de lo que se le pase cuando se llame a la función
    # Si la lista de nombres está vacía, lanzamos un error para evitar escribir un archivo vacío
    if len(nombres) == 0:
        raise ValueError("No se ha proporcionado ningún nombre")

    # Abrimos el archivo en modo 'a' (append) para añadir contenido al final sin borrar lo anterior
    with open(archivo, 'a') as file:
        # Recorremos cada nombre de la lista
        for name in nombres:
            # Escribimos el nombre en el archivo, añadiendo un salto de línea al final
            file.write(f"{name}\n")

#Aquí es donde realmente se define el tipo de nombres
nombres = input("Introduce una lista de nombres separados por espacio: \n").split()
# Llamamos a la función, pasando la lista de nombres y el nombre del archivo donde guardarlos
escribir_nombres_en_archivo(nombres, "nombres.txt")



#Si quiero sobrescribir el archivo (borrar lo anterior y empezar de cero), cambiar el modo 'a' por 'w':