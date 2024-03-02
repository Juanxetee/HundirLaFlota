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
        self.tablero_visible = np.zeros((self.dimensiones, self.dimensiones), dtype=int)  # Tablero visible para el jugador, donde se muestran los disparos realizados.
        self.tablero_oculto = np.zeros((self.dimensiones, self.dimensiones), dtype=int)   # Tablero oculto con los barcos del oponente y no se muestra al jugador.

#Este método verifica si una posición dada en el tablero oculto es válida para colocar un barco. Toma una fila, columna, orientación y longitud como parámetros.
    def validar_posicion(self, fila, columna, orientacion,longitud):
        if orientacion == 'N':
            if fila - longitud + 1 < 0: #verifica si colocar el barco excede los limites por arriba
                return False
            for i in range(longitud):
                if self.tablero_oculto[fila - i, columna] != 0:  #verifica si hay otro barco en las posiciones donde se intenta colocar este
                    return False
            for i in range(longitud):
                self.tablero_oculto[fila - i, columna] = 1
        elif orientacion == 'S':
            if fila + longitud > self.dimensiones:
                return False
            for i in range(longitud):
                if self.tablero_oculto[fila + i, columna] != 0:
                    return False
            for i in range(longitud):
                self.tablero_oculto[fila + i, columna] = 1
        elif orientacion == 'O':
            if columna - longitud + 1 < 0:
                return False
            for i in range(longitud):
                if self.tablero_oculto[fila, columna - i] != 0:
                    return False
            for i in range(longitud):
                self.tablero_oculto[fila, columna - i] = 1
        elif orientacion == 'E':
            if columna + longitud > self.dimensiones:
                return False
            for i in range(longitud):
                if self.tablero_oculto[fila, columna + i] != 0:
                    return False
            for i in range(longitud):
                self.tablero_oculto[fila, columna + i] = 1
        return True
    
#Este método inicializa el tablero colocando los barcos en posiciones aleatorias en el tablero oculto.
    def inicializar_tablero(self):
        # Colocar los barcos en el tablero oculto
        for barco, longitud in self.barcos.items(): #bucle for para iterar sobre los barcos definidos en variables
            colocado = False
            while not colocado: #genera aleatoriamente una fila y columna de inicio, así como una orientación, seguira en bucle hasta colocar
                fila = np.random.randint(0, self.dimensiones)
                columna = np.random.randint(0, self.dimensiones)
                orientacion = np.random.choice(["N","S","O","E"])

                if self.validar_posicion(fila, columna, orientacion, longitud): #verifica si la posición es válida utilizando el método validar_posicion 
                   colocado = True #si es válida, coloca el barco en el tablero oculto.
                


    def generar_barco_aleatorio(self, tablero, longitud): 
        #filas, columnas = tablero.shape
        fila = np.random.randint(0, filas - 1)
        columna = np.random.randint(0, columnas - 1)
        orientacion = np.random.choice(['N', 'S', 'O', 'E'])
        while not self.validar_posicion(fila, columna, orientacion): # Va a llamar a la funcion posicionar barco hasta que devuelva true, una vez sea true otorga los valores random en el lugar que dio true
            fila = np.random.randint(0, filas - 1)
            columna = np.random.randint(0, columnas - 1)
            orientacion = np.random.choice(['N', 'S', 'O', 'E'])


if __name__ == "__main__": 
    tab1 = Tablero(1)
    print(tab1.tablero_oculto)


