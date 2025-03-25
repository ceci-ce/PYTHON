# #1. Longitud de una cadena
#
# """nombre = "Cecilia"
# print("Longitud del nombre: ",len(nombre))
#
# #2. Convertir texto a mayusculas y minusculas
# #upper
# print("Esto soy yo en mayusculas: ",nombre.upper())
# #lower
# print("Esto soy yo en minúsculas: ", nombre.lower())"""

#Ejercicios con estas utilidades combinadas

"""1. Generador de nombres de usuario
Pide al usuario su nombre y apellido.
Genera un nombre de usuario en minúsculas, sin espacios.
Añade un número aleatorio al final.
Muestra el nombre de usuario generado. """

nombre = "Cecilia"
apellido ="de la Cámara"
nombre_de_usuario = f"{nombre}{apellido}" #Usar un f-string para concatenar sin espacios
import random

print("Escribe tu nombre y apellido: ", nombre, apellido)
print("Tu nombre de usuario es: ", nombre_de_usuario.lower().replace(" ",""),random.randint(1,50))

"""2. Analizador de frases
Pide al usuario que ingrese una frase.
Muestra la cantidad de caracteres de la frase.
Indica si la frase contiene la palabra "Python".
Convierte la frase a mayúsculas.
Muestra la frase invertida.
"""

frase = "Está lloviendo demasiado"
palabras = ["Demasiado", "lloviendo","está"]

print("Escribe una frase sobre lo que estás pensando: ",frase)
print("La cantidad de caracteres de la frase es de: ",len(frase))
print("¿Contiene la frase la palabra Python?: ", ("Python" in frase))
print("La frase en mayúsculas es: " , frase.upper())
print("La frase invertida es: ", " ".join(palabras))

"""3. Cálculo de descuentos
Pide al usuario el precio de un producto.
Aplica un 15% de descuento.
Muestra el precio final con dos decimales.
Muestra el precio redondeado hacia arriba.
"""

precio_mascarilla = 4.5
descuento = ((15/100)*precio_mascarilla)
import math

print("Con el descuento del 15%, el precio de la mascarilla se queda en ", (4.5-
      round(descuento,2)), "€")
print("El precio redondeado hacia arriba es de ", math.ceil(precio_mascarilla), "€")

"""4. Generador de etiquetas de productos
Pide el nombre de un producto y su precio.
Convierte el nombre del producto a mayúsculas.
Muestra el precio con dos decimales.
Genera un código basado en el valor ASCII de la primera letra del producto.
"""

nombre_producto = "colorete Rhode"
precio_colorete = 32.50

print(nombre_producto.upper())
print("El precio con dos decimales es: {:.2f}".format(precio_colorete))
print("El valor ASCII de la primera letra del producto es ",ord(nombre_producto[:1]))

"""5. Conversión de tipos y manipulación de listas
Pide al usuario una lista de números separados por comas.
Convierte cada número a entero.
Elimina los números repetidos."
Muestra la lista ordenada sin duplicados.
"""
numeros_decimales = [4.3,5.2,9.2,4.3,1.4,5.2,9.0]
sin_duplicados = set(numeros_decimales)
# numeros_enteros = ((numeros_decimales) // 1 )) No se me ocurre como convertir los numeros decimales a enteros
# print(numeros_enteros)

print("Lista sin duplicados:",sin_duplicados)

"""6. Creación de mensajes personalizados
Pide al usuario su nombre, edad y ciudad.
Muestra un mensaje con toda la información.
Si la edad es menor de 18, redondea hacia arriba hasta la mayoría de edad.
"""

edad = 27
ciudad = "Madrid"

print(f"Hola, mi nombre es {nombre} tengo {edad} años y vivo en {ciudad}.")

"""7. Generador de contraseñas aleatorias
Pide al usuario su nombre.
Genera una contraseña segura con la primera letra en mayúscula, un número aleatorio y un símbolo especial.
Muestra la contraseña generada.
"""

contraseña = f"{nombre[:1].upper()}{random.randint(7,30)}@"

print("La contraseña del usuario es ", contraseña)

"""8. Verificación de nombres en listas
Pide al usuario su nombre.
Verifica si su nombre está en una lista de invitados predefinida.
Si está en la lista, muestra su posición.
"""

lista_invitados = ["Alejandro","Margarita",nombre,"Amanda","Marcos"]
print("¿Está Cecilia invitada a la fiesta?",(nombre in lista_invitados))

"""9. Manipulación de nombres
Pide al usuario su nombre y apellido.
Convierte el nombre a minúsculas y el apellido a mayúsculas.
Genera un alias combinando las primeras 3 letras del nombre y del apellido.
Muestra el alias generado.

"""
"""nombre = input("Escribe tu nombre ")
apellido = input("Escribe tu apellido ")

alias = nombre[:3].lower(),apellido[:3].upper()
print(f"El alias del usuario es {alias}")"""

"""10. Formatear y mostrar datos matemáticos
Pide al usuario un número decimal.
Muestra el número redondeado a dos decimales.
Calcula y muestra su cuadrado.
Calcula y muestra su raíz cuadrada.
"""
"""numero_decimal = float(input("Escribe un numero decimal "))

print("Numero redondeado ",round(numero_decimal,2))
print(f"Cuadrado: {numero_decimal**2}")
print("Raiz cuadrada ", (numero_decimal**0.5))"""