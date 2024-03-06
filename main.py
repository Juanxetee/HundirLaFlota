from clases import Tablero
import funciones

def main():
    # Inicialización de tableros
    tablero_jugador = Tablero("Jugador")
    tablero_maquina = Tablero("Máquina")
    tablero_jugador.inicializar_tablero()
    tablero_maquina.inicializar_tablero()

    print("¡Bienvenido a Hundir la Flota!")
    print("Instrucciones:")
    print(" - 'O' representa agua")
    print(" - 'X' representa un barco impactado")
    print()

    while True:
        # Turno del jugador
        print("Tu turno:")
        mostrar_tablero(tablero_jugador.tablero_visible)
        fila, columna = obtener_coordenadas()
        turno_jugador(tablero_maquina, fila, columna)
        if juego_terminado(tablero_maquina):
            print("¡Has ganado!")
            break

        # Turno de la máquina
        print("Turno de la máquina:")
        turno_maquina(tablero_jugador)
        if juego_terminado(tablero_jugador):
            print("¡La máquina ha ganado!")
            break

if __name__ == "__main__":
    main()
           

