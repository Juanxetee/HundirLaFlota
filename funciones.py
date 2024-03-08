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
        except ValueError: #lo incluimos por si el jugador mete valores no numericos
            print("Por favor, introduce valores numéricos válidos.")

# Función para el turno del jugador
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

# Función para el turno de la máquina
def turno_maquina(tablero_visible_maquina):
    while True:
        fila = np.random.randint(0, tablero_visible_maquina.dimensiones)
        columna = np.random.randint(0, tablero_visible_maquina.dimensiones)
        impacto = tablero_visible_maquina.disparo_coordenada_maquina(fila, columna)  
        print(f"La máquina dispara en la fila {fila} y columna {columna}")
        if impacto:
            print("¡La máquina ha impactado en uno de tus barcos!")
        else:
            print("La máquina ha dado en el agua...")
            break

# Función para verificar si el juego ha terminado
def juego_terminado(tablero_jugador, tablero_maquina):
    return np.sum(tablero_jugador.tablero_oculto_jugador == 1) == 0 or np.sum(tablero_maquina.tablero_oculto_maquina == 1) == 0