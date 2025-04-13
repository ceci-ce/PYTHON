# Ejercicio 3 - Pacman¶
# Escribe un programa que pida al usuario dos números enteros correspondientes a la casilla que está Pacman (1er número)
# y a la que está un fantasma (2o número), luego debe recibir un texto con el formato "normal" o "caramelo". Si el texto
# es "normal" y los números son iguales, el programa debe imprimir "Pacman ha sido atrapado". Si el texto es "caramelo"
# y los números son iguales, el programa debe imprimir "Pacman ha comido al fantasma". En cualquier otro caso, el
# programa debe imprimir "Pacman ha escapado".

pos_pacman = int(input("Cual es la posicion de Pacman? "))
pos_fantasma = int(input("Cual es la posicion del fantasma? "))

if pos_pacman == pos_fantasma:
    # Caramelo -> Pacman come fantasma
    # Invisible -> Pacman escapa
    # Normal -> Pacman atrapado
    estado_pacman = input("Como está Pacman? ")
    if estado_pacman == "caramelo":
        print("Pacman ha comido al fantasma")
    elif estado_pacman == "invisible":
        print("Pacman ha escapado")
    else:
        print("Pacman ha sido atrapado")
else:
    print("Pacman ha escapado")