from variables import barcos, dimensiones
from clases import Tablero

import numpy as np

def obtener_coordenadas():
    while True:
        try:
            fila = int(input("Introduce la fila (0-9): "))
            columna = int(input("Introduce la columna (0-9): "))
            if 0 <= fila < dimensiones and 0 <= columna < dimensiones:
                return fila, columna
            else:
                print("Coordenadas fuera de rango. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, introduce valores numéricos válidos.")

def turno_jugador(tablero, fila, columna):
    while True:
        impacto = tablero.disparo_coordenada_jugador(fila, columna)
        tablero.mostrar_tablero_jugador()
        if impacto:
            print("¡Has impactado en un barco!")
            fila, columna = obtener_coordenadas()  # Vuelve a pedir coordenadas
        else:
            print("Agua...")
            break  # Si no hay impacto en un barco, el turno del jugador termina

def turno_maquina(tablero_jugador, tablero_maquina):
    while True:
        fila = np.random.randint(0, tablero_jugador.dimensiones)
        columna = np.random.randint(0, tablero_jugador.dimensiones)
        impacto = tablero_jugador.disparo_coordenada_jugador(fila, columna)  # Cambio aquí
        print(f"La máquina dispara en la fila {fila} y columna {columna}")
        if impacto:
            print("¡La máquina ha impactado en uno de tus barcos!")
            tablero_maquina.tablero_visible_jugador[fila, columna] = "X"  # Actualiza el tablero visible del jugador
        else:
            print("La máquina ha dado en el agua...")
            tablero_maquina.tablero_visible_jugador[fila, columna] = "."  # Actualiza el tablero visible del jugador
            break

def juego_terminado(tablero_jugador, tablero_maquina):
    return np.sum(tablero_jugador.tablero_oculto_jugador) == 0 or np.sum(tablero_maquina.tablero_oculto_maquina) == 0