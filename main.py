from clases import Tablero
from funciones import obtener_coordenadas, turno_jugador, turno_maquina, juego_terminado

#Este es el punto de entrada del juego. Inicializa los tableros para el jugador y la máquina, imprime las instrucciones del juego y entra en un bucle donde se alternan los turnos
#del jugador y la máquina. El juego continúa hasta que uno de los jugadores hunde todos los barcos del oponente.
def main():
    #inicializamos los tableros
    tablero_jugador = Tablero("Jugador") # creamos la identidad del jugador y la maquina
    tablero_maquina = Tablero("Máquina")

    print("¡Bienvenido a Hundir la Flota!")
    print("Instrucciones:")
    print(" - 'X' representa un barco impactado")
    print(" - '.' representa agua")
    print()

    while True:
        print("Tu turno:")
        tablero_jugador.mostrar_tablero_jugador() #mostramos tablero del jugador
        fila, columna = obtener_coordenadas() # solicitiamos al jugador fila y columna para disparar
        turno_jugador(tablero_maquina, fila, columna) #llamamos a turno jugador para registrar el disparo y mostrar el resultado
        if juego_terminado(tablero_jugador, tablero_maquina): # verificamos que aun queden barcos del rival
            print("¡Has ganado!") # en caso de que no, es victoria para el jugador
            break #salimos del bucle con un break

        print("Turno de la máquina:")  #repetimos mismo proceso pero siendo la maquina quien genera disparo aleatorio
        turno_maquina(tablero_jugador, tablero_maquina)
        if juego_terminado(tablero_jugador, tablero_maquina):
            print("¡La máquina ha ganado!")
            break

if __name__ == "__main__":
    main()

