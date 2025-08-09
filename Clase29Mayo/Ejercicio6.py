"""Ejercicio 6 - Elecciones a delegado¶
Escribe un programa que simule unas elecciones a delegado de clase. El programa debe permitir a los alumnos votar por
un candidato introduciendo su nombre. Al finalizar la votación, el programa debe mostrar el nombre del candidato ganador
y el número de votos obtenidos. Si hay un empate, el programa debe informar al usuario del primer candidato que alcanzó
el número máximo de votos. El programa debe ejecutarse indefinidamente hasta que el usuario introduzca "FIN VOTACIONES"."""

votos = {}

max_votos = 0
ganador = None


while True:
    entrada = input("Introduce el nombre del candidato (o 'FIN VOTACIONES' para terminar): ").strip().lower()

    if entrada.upper() == "FIN VOTACIONES":
        break

    # sumar un voto al candidato

    candidato = entrada.lower()
    if candidato in votos:
        votos[candidato] += 1  #Si ya existe una clave con el nombre del candidato, se le suma 1
    else:
        votos[candidato] = 1  #Si no existe, significa que es el primer voto que recibe el candidato, asi que lo añadimos al diccionario con valor 1.

        # actualización del ganador: solo si supera el máximo actual

    if votos[candidato] > max_votos:
        max_votos = votos[candidato] # actualizamos el número más alto encontrado
        ganador = candidato          # actualizamos quién es el ganador

    # si votos[clave] == max_votos -> no hacemos nada, así mantenemos al que llegó primero

    # resultado final
    if votos:
        print(f"\nEl ganador es {ganador.title()} con {max_votos} votos.")
    else:
        print("No se registraron votos.")

