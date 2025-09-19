# Iniciales de un nombre

nombre =input("Cual es tu nombre?")
palabras = nombre.split()
iniciales = "".join([p[0].upper() for p in palabras])
print(iniciales)