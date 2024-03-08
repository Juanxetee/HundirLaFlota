from clases import Tablero
from funciones import obtener_coordenadas, turno_jugador, turno_maquina, juego_terminado

#Este es el punto de entrada del juego. Inicializa los tableros para el jugador y la máquina, imprime las instrucciones del juego y entra en un bucle donde se alternan los turnos
#del jugador y la máquina. El juego continúa hasta que uno de los jugadores hunde todos los barcos del oponente.
def main():
    # Inicializa los tableros para el jugador y la máquina
    tablero_jugador = Tablero("Jugador")
    tablero_maquina = Tablero("Máquina")

    # Muestra las instrucciones del juego
    print("¡Bienvenido a Hundir la Flota!")
    print("Instrucciones:")
    print(" - 'X' representa un barco impactado")
    print(" - '.' representa agua")
    print("¡Hunde al completo la flota enemiga para ganar!")
    print()

    # Bucle principal del juego
    while True:
        print("Tu turno:")
        tablero_jugador.mostrar_tablero_jugador()  # Muestra el tablero del jugador
        fila, columna = obtener_coordenadas()  # Solicita al jugador fila y columna para disparar
        turno_jugador(tablero_maquina, fila, columna)  # Realiza el turno del jugador y muestra el resultado
        if juego_terminado(tablero_jugador, tablero_maquina):  # Verifica si aún quedan barcos del rival
            print("¡Has ganado!")  # Si no quedan barcos, es victoria para el jugador
            break  # Sale del bucle

        print("Turno de la máquina:")  # Repite el proceso para el turno de la máquina
        turno_maquina(tablero_jugador)
        if juego_terminado(tablero_jugador, tablero_maquina):
            print("¡La máquina ha ganado!")
            break

if __name__ == "__main__":
    main()