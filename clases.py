import numpy as np 
from variables import dimensiones_tablero, barcos # Importamos las variables desde variables.py
 
#Aquí definimos la clase Tablero, que representa el tablero de juego para un jugador. La clase tiene métodos para inicializar el tablero con los barcos y
# validar posiciones. Utiliza la biblioteca numpy para manejar matrices.

class Tablero:
#Tenemos un constructor que inicializa las propiedades del tablero, id del jugador, las dimensiones del tablero, los barcos y dos matrices numpy: tablero visible y tablero oculto.
    def __init__(self, id_jugador):
        self.id_jugador = id_jugador
        self.dimensiones = dimensiones_tablero
        self.barcos = barcos
        self.tablero_visible = np.zeros((self.dimensiones, self.dimensiones), dtype=str)  # Tablero visible para el jugador, donde se muestran los barcos del jugador y los disparos de la maquina
        self.tablero_oculto = np.zeros((self.dimensiones, self.dimensiones), dtype=int)   # Tablero oculto con los barcos del oponente ocultos, en este tablero se veran los disparos del jugador
        

#Este método verifica si una posición dada en el tablero oculto es válida para colocar un barco. Toma una fila, columna, orientación y longitud como parámetros.
    def validar_posicion(self, fila, columna, orientacion,longitud,tablero):
        if orientacion == 'N': #
            if fila - longitud + 1 < 0: #verifica si colocar el barco excede los limites por arriba
                return False
            for i in range(longitud):
                if self.tablero_visible[fila - i, columna] != "o":  #verifica si hay otro barco en las posiciones donde se intenta colocar este
                    return False
        elif orientacion == 'S':
            if fila + longitud > self.dimensiones:
                return False
            for i in range(longitud):
                if self.tablero_visible[fila + i, columna] != "o":
                    return False
        elif orientacion == 'O':
            if columna - longitud + 1 < 0:
                return False
            for i in range(longitud):
                if self.tablero_visible[fila, columna - i] != "o":
                    return False
        elif orientacion == 'E':
            if columna + longitud > self.dimensiones:
                return False
            for i in range(longitud):
                if self.tablero_visible[fila, columna + i] != "o":
                    return False
        return True
    
#Este método inicializa el tablero colocando los barcos en posiciones aleatorias en el tablero oculto
    def inicializar_tablero(self):
        # Colocar los barcos en el tablero oculto
        for barco, longitud in self.barcos.items(): #bucle for para iterar sobre los barcos definidos en variables
            colocado = False
            while not colocado: #genera aleatoriamente una fila y columna de inicio, así como una orientación, seguira en bucle hasta colocar
                fila = np.random.randint(0, self.dimensiones)
                columna = np.random.randint(0, self.dimensiones)
                orientacion = np.random.choice(["N","S","O","E"])

                if self.validar_posicion(fila, columna, orientacion, longitud,self.tablero_visible):
                    if orientacion == 'N':
                        for i in range(longitud):
                            self.tablero_visible[fila - i, columna] = "o"
                    elif orientacion == 'S':
                        for i in range(longitud):
                            self.tablero_visible[fila + i, columna] = "o"
                    elif orientacion == 'O':
                        for i in range(longitud):
                            self.tablero_visible[fila, columna - i] = "o"
                    elif orientacion == 'E':
                        for i in range(longitud):
                            self.tablero_visible[fila, columna + i] = "o"
                    colocado = True #verifica si la posición es válida utilizando el método validar_posicion, si es válida, coloca el barco en el tablero propio
                
    def disparo_coordenada(self, fila, columna):
        if self.tablero_oculto[fila, columna] == "o":
            self.tablero_oculto[fila, columna] = "x"  # Cambia el estado del tablero oculto para mostrar el impacto
            self.tablero_visible[fila, columna] = "x"  # Cambia el estado del tablero visible para mostrar el impacto
            return True
        else:
            self.tablero_oculto[fila, columna] = "-"  # Cambia el estado del tablero oculto para mostrar el disparo del oponente
            self.tablero_visible[fila, columna] = '-'
            return False             


if __name__ == "__main__": 
    tab1 = Tablero(id_jugador="juancho")
    print(tab1.inicializar_tablero())
    print("Tablero antes de los disparos:")
    print(tab1.tablero_visible)
    print("\n")
    coordenadas_disparos = [(0, 0), (2, 3), (5, 5)]
    for coordenada in coordenadas_disparos:
        fila, columna = coordenada
        impacto = tab1.disparo_coordenada(fila, columna)
        if impacto:
            print(f"¡Impacto en la coordenada {coordenada}!")
        else:
            print(f"Disparo en la coordenada {coordenada}, sin impacto.")

    # Mostrar el tablero después de los disparos
    print("\n")
    print("Tablero después de los disparos:")
    print(tab1.tablero_visible)
    print(tab1.tablero_oculto)




