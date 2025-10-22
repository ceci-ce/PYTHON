import os.path

# Ejercicio 4 - Copiar el contenido de un archivo a otro¶
# Escribe un programa que copie el contenido de un archivo de texto a otro archivo. El programa debe definir una función
# que reciba los nombres de ambos archivos, lea el contenido del primer archivo y lo escriba en el segundo archivo.

def copy_file(file1, file2):
    if not os.path.exists(file1):
        raise FileNotFoundError("El archivo a copiar no existe")

    with open(file1, 'r') as file1:
        lines_line1 = file1.readlines()
        if len(lines_line1) == 0:
            raise ValueError("El archivo a copiar está vacío")

        if os.path.exists(file2):
            answer = input(f"El archivo {file2} ya existe, ¿desea sobreescribir? Y/N\n")
            if answer.upper() == "N":
                return

        with open(file2, 'w') as file2:
            file2.writelines(lines_line1)

file_to_copy = input("Introduce el nombre del archivo a copiar: \n")
new_copied_file = input("Introduce el nombre del nuevo archivo: \n")

copy_file(file_to_copy, new_copied_file)
