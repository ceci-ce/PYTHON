import os

def listar_archivos():
    os.listdir(".")

def main():
    opcion = -1
    while opcion != 5:
        print("### MENU ###")
        print("1. Listar archivos")
        print("2. Verificar existencia archivos")
        print("3. Crear archivos")
        print("4. Crear directorio")
        print("5. Salir")

        opcion = int(input("Escoge una opcion:\n"))




if