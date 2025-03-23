"""Ejercicio 1: Operaciones numéricas complejas
Define cinco variables numéricas distintas (int, float, complex)
y realiza diversas operaciones matemáticas (potenciación, división entera, módulo).
Imprime los resultados formateados en una cadena clara y descriptiva."""

numero_int = 21
numero_float = 23.64
numero_complex = 5 + 6j

print("Ejemplo de multiplicacion entre numero entero y decimal es: ", (numero_int*numero_float))
print("El resultado de la division entre un numero decimal y uno complejo es: ",(numero_float/numero_complex))
print("El resultado de la division entera entre un numero decimal y uno entero es: ", (numero_float//numero_int))

resultado = f"Multiplicacion: {numero_float*numero_int}, Division entera: {numero_float//numero_int}, Modulo: {numero_float%numero_int}"
print(resultado)

"""Ejercicio 2: Combinación de cadenas y números
Define dos variables numéricas (int, float) y tres cadenas diferentes. Genera una nueva cadena combinando
texto con el resultado de operaciones aritméticas entre estas variables. 
Usa conversión explícita (str()) para insertar valores numéricos en la cadena final."""

num_int = 12
num_float = 58.69
cadena_1 = "El resultado de "
cadena_2 = "la suma es: "
cadena_3 = " y la division es: "

resultado2 = cadena_1 + cadena_2 + str(num_int+num_float) + cadena_3 + str(num_int/numero_float)
print(resultado2)

"""Ejercicio 3: Manipulación avanzada de cadenas
Crea una cadena larga que contenga espacios en blanco al inicio, final, y en medio. 
Realiza varias operaciones encadenadas como eliminar espacios extremos, convertir todo a mayúsculas, y 
dividir la cadena en varias subcadenas usando un separador específico."""

cadena_4 = "  Ejemplo de cadena larga con espacios  "
nueva_cadena4 = cadena_4.upper().strip().split()
print(nueva_cadena4)

"""Ejercicio 4: Índices y subcadenas
Define una cadena extensa (mínimo 50 caracteres). Obtén varias subcadenas usando la indexación por rangos (slicing) 
y genera una nueva cadena combinando estas subcadenas en orden inverso. Imprime la nueva cadena resultante."""

cadena_5 = ("Esto es una prueba de cadena larga con 50 caracteres para probar el metodo slicing y crear una nueva cadena"
            "en orden inverso")
subcadena_5 = cadena_5[0:8], cadena_5[-24],cadena_5[20:38]
resultado_subcadena5 = subcadena_5[::-1]
print(resultado_subcadena5)

"""Ejercicio 5: Formato y conversión numérica
Define variables numéricas (entero, flotante, complejo). Crea una cadena con formato avanzado (f-strings) 
que muestre estos números con precisión definida (dos decimales, notación científica, etc.). 
Evita concatenar directamente números y texto."""

numero_int2 = 13
numero_float2 = 12.49667785
numero_complex2 = 2 + 2j

cadena_6 = f"La suma es {(numero_int2) + (numero_float2)} , la multiplicacion es {(numero_complex2) * (numero_int2)}"
print(cadena_6) # Prueba de operaciones(en realidad me equivoqué)

resultado3 = (f"Entero: {numero_int2}, Decimal: {numero_float2:.2f}, Notacion cientifica: {numero_float2:.2e}, "
            f"Complejo: {numero_complex2}")
print(resultado3)

"""Ejercicio 6: Operaciones combinadas entre números y cadenas
Define dos variables numéricas enteras y dos cadenas. Realiza cálculos matemáticos diversos 
y genera una cadena formateada que explique cada operación (sumas, restas, multiplicaciones, módulo) claramente 
utilizando métodos de cadenas."""

numero_int3 = 20
numero_int4 = 30
cadena_8 = "La suma da "
cadena_9 = "la multiplicacion da "
cadena_10 = "la resta da "
cadena_11 = "y el resto es "

resultado4 = f"{cadena_8}{numero_int3 + numero_int4}, {cadena_9}{numero_int3 * numero_int4}, {cadena_10}{numero_int4
-numero_int3}, {cadena_11}{numero_int4 % numero_int3}"
print(resultado4)

"""Ejercicio 7: Cálculo del área y perímetro
Define variables numéricas que representen dimensiones (largo, ancho, radio, altura). Calcula el área y
perímetro de distintas figuras geométricas (rectángulo, círculo, triángulo rectángulo) y presenta todos los resultados 
claramente en una sola cadena formateada usando conversiones explícitas."""

largo, ancho, radio, altura = 10, 5, 3, 4
area_rectangulo = largo * ancho
perimetro_rectangulo = 2 * (largo + ancho)
area_circulo = 3.14159 * radio ** 2
perimetro_circulo = 2 * 3.14159 * radio
area_triangulo = (largo * altura)/2

resultado5 = (f"Rectangulo: area {area_rectangulo}, perimetro {perimetro_rectangulo}. Circulo: area {area_circulo}, "
              f"perimetro {perimetro_circulo}. Triangulo: area {area_triangulo}")
print(resultado5)

"""Ejercicio 8: Análisis de texto complejo
Define una cadena extensa que represente un párrafo completo. Utilizando únicamente métodos de cadenas 
y funciones integradas (len, upper, split), obtén el número total de caracteres, palabras y el resultado de 
transformar el texto completamente a mayúsculas, presentándolo claramente en una cadena nueva."""

parrafo_completo = ("Pues no se que escribir se me acaban las ideas, estamos con el ejercicio numero 8 y solo me quedarian "
                    "dos mas para terminar.")

caracteres = len(parrafo_completo)
palabras = len(parrafo_completo.split())
mayusculas = parrafo_completo.upper()

parrafo_nuevo = (f"El total de caracteres del texto es {caracteres}, de palabras es {palabras} y el texto en mayusculas "
                 f"es {mayusculas}")
print(parrafo_nuevo)

"""Ejercicio 9: Fórmula cuadrática
Dados tres números que representan los coeficientes (a, b, c) de una ecuación cuadrática, resuelve la fórmula 
cuadrática para obtener las raíces reales o complejas. Imprime claramente en una cadena formateada los coeficientes 
y las raíces encontradas."""

a = 1
b = -3
c = 2
discriminante = (b**2-4* a * c) ** 0.5
raiz1 = (-b + discriminante)/(2*a)
raiz2 = (-b - discriminante)/(2*a)
resultado6 = f"Coeficientes: a= {a},b= {b},c = {c}.Raices:{raiz1},{raiz2}"
print(resultado6)

"""Ejercicio 10: Manejo y transformación de datos personales
Crea variables para representar datos personales (nombre, edad, peso, altura). Calcula el índice de masa corporal (IMC)
sin usar bucles, y presenta un resumen detallado y formateado de todos estos datos personales, incluyendo el 
IMC con dos decimales."""

nombre = "Claudia"
edad = 32
peso = 55
altura = 1.57
imc = (peso/altura)

resultado7 = f"El IMC de {nombre} de {edad} años de edad es de {imc:.2f}"
print(resultado7)
