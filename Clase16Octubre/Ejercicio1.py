import os # os permite comprobar existencia de archivos, rutas...

def count_lines(path): # se define una función que recibirá la ruta a un archivo y devolverá el número de líneas
     if not os.path.exists(path):
         raise FileExistsError("El archivo no existe") #raise sirve para lanzar (generar) una excepción manualmente
                #Cuando Python encuentra un raise, interrumpe la ejecución normal y busca un bloque try/except que pueda manejar ese error.

     with open(path, 'r') as file: #abre un archivo y crea una variable temporal (file) para trabajar con él
         return len(file.readlines()) #file.readlines() lee todas las líneas en memoria y devuelve una lista; len(...) da el número de líneas.

     #    1.Abre el archivo indicado por path en modo lectura ('r').
     #    2.Lee todas las líneas con file.readlines().
     #    3.Devuelve el número total con len(...).
     #    4.Cierra automáticamente el archivo al salir del with.

try:
    print(f"El numero de lineas del archivo ejemplo.txt es {count_lines('ejemplo.txt')}")
except Exception as e:
    print(e)