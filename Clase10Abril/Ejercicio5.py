# Ejercicio 5 - Puede entrar en el servidor de Discord?¶
# Escribe un programa que pida un rol y una academia de estudios, si el rol es "alumno" y la academia es "Prometeo" el
# programa debe darle acceso al servidor de Discord oficial y al de los alumnos, donde se critica a los profes. Si el rol
# es "profesor" y la academia es "Prometeo" el programa debe darle acceso al servidor de Discord oficial, pero no al de
# los alumnos. En cualquier otro caso, el programa debe imprimir "No tienes acceso al servidor de Discord".

rol = input("Qué rol tienes?: ").lower()
academia = input("Cual es tu academia?: ").lower()

if rol == "alumno" and academia == "prometeo":
    print("Tienes acceso al Discord oficial y al de alumnos")
elif rol == "profesor" and academia == "prometeo":
    print("Solo tienes acceso al Discord oficial")
else:
    print("No tienes acceso al servidor de Discord")