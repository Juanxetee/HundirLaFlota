from clases import Tablero
import funciones

#Este es el punto de entrada del juego. Inicializa los tableros para el jugador y la máquina, imprime las instrucciones del juego y entra en 
# un bucle donde se alternan los turnos del jugador y la máquina. El juego continúa hasta que uno de los jugadores hunde todos los barcos del oponente.
def main():
    # Inicialización de tableros
    tablero_jugador = Tablero("Jugador") # Creamos dos instancias de la clase Tablero, una para el jugador 
    tablero_maquina = Tablero("Máquina") # otra para la máquina
    tablero_jugador.inicializar_tablero() # inicializamos los tableros llamando al método inicializar_tablero en cada uno
    tablero_maquina.inicializar_tablero()

    print("¡Bienvenido a Hundir la Flota!")
    print("Instrucciones:")
    print(" - '-' representa agua")
    print(" - 'X' representa un barco impactado")
    print()

    while True:
        # Turno del jugador
        print("Tu turno:")
        mostrar_tablero(tablero_jugador.tablero) #Mostramos el tablero visible del jugador
        fila, columna = obtener_coordenadas() #solicitamos al jugador que ingrese las coordenadas del disparo
        turno_jugador(tablero_maquina, fila, columna) #llamamos a la función turno_jugador para registrar el disparo y mostrar el resultado.
        if juego_terminado(tablero_maquina): #Después del turno del jugador, verificamos si todos los barcos de la máquina han sido hundidos. 
            print("¡Has ganado!") #si es asi, imprimimos un mensaje de victoria para el jugador
            break #salimos del bucle con break.

        # Turno de la máquina
        print("Turno de la máquina:")
        turno_maquina(tablero_jugador) # llamamos a la funcion turno_maquina para que realice un disparo
        if juego_terminado(tablero_jugador): # Mismo proceso de verificacion depues del turno pero para la maquina
            print("¡La máquina ha ganado!")
            break

if __name__ == "__main__":
    main()
           

