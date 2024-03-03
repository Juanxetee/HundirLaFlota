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
        self.tablero = np.zeros((self.dimensiones, self.dimensiones), dtype=str)  # Tablero visible para el jugador, donde se muestran los barcos del jugador y los disparos de la maquina
        self.tablero_oculto = np.zeros((self.dimensiones, self.dimensiones), dtype=int)   # Tablero oculto con los barcos del oponente ocultos, en este tablero se veran los disparos del jugador
        

#Este método verifica si una posición dada en el tablero oculto es válida para colocar un barco. Toma una fila, columna, orientación y longitud como parámetros.
    def validar_posicion(self, fila, columna, orientacion,longitud,tablero):
        #MF: como queremos verificar posición en tablero oculto, usamos tablero o mejor tablero_oculto?
        if orientacion == 'N': #
            if fila - longitud + 1 < 0: #verifica si colocar el barco excede los limites por arriba
            #MF: por revisar si tiene que ser <=0 fila 1 dimensión 2. 1-2+1=0.   
                return False
            for i in range(longitud):
                if tablero[fila - i, columna] != '':  #verifica si hay otro barco en las posiciones donde se intenta colocar este
                    return False
        elif orientacion == 'S':
             #MF: por revisar si tiene que ser columna+longitud -1 >= self.dimensiones. fila 9 dimensión 2. 9+2=11 que 11>10 si ponemos 9+2-1=10  10>=10                   
            if fila + longitud > self.dimensiones:
                return False
            for i in range(longitud):
                if tablero[fila + i, columna] != '':
                    return False
        elif orientacion == 'O':
            #MF: por revisar si tiene que ser <=0. colunma 2 dimensión 3. 2-3+1=0
            if columna - longitud + 1 < 0:
                return False
            for i in range(longitud):
                if tablero[fila, columna - i] != '':
                    return False
        elif orientacion == 'E':
             #MF: por revisar si tiene que ser columna+longitud -1 >= self.dimensiones. colunma 9 dimensión 3. 9+2=11 que 11>10         
            if columna + longitud > self.dimensiones:
                return False
            for i in range(longitud):
                if tablero[fila, columna + i] != '':
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

                if self.validar_posicion(fila, columna, orientacion, longitud,self.tablero):
                    if orientacion == 'N':
                        for i in range(longitud):
                            self.tablero[fila - i, columna] = "O"
                            self.tablero_oculto[fila - i, columna] = 1
                    elif orientacion == 'S':
                        for i in range(longitud):
                            self.tablero[fila + i, columna] = "O"
                            self.tablero_oculto[fila + i, columna] = 1
                    elif orientacion == 'O':
                        for i in range(longitud):
                            self.tablero[fila, columna - i] = "O"
                            self.tablero_oculto[fila, columna - i] = 1
                    elif orientacion == 'E':
                        for i in range(longitud):
                            self.tablero[fila, columna + i] = "O"
                            self.tablero_oculto[fila, columna + i] = 1
                    colocado = True #verifica si la posición es válida utilizando el método validar_posicion, si es válida, coloca el barco en el tablero propio
                
    def disparo_coordenada(self, fila, columna):
        if self.tablero_oculto[fila, columna] == 1:
            self.tablero_oculto[fila, columna] = 2  # Cambia el estado del tablero oculto para mostrar el impacto
            self.tablero[fila, columna] = "X"  # Cambia el estado del tablero visible para mostrar el impacto
            return True
        else:
            self.tablero_oculto[fila, columna] = 3  # Cambia el estado del tablero oculto para mostrar el disparo del oponente
            self.tablero[fila, columna] = '~'
            return False             


if __name__ == "__main__": 
    tab1 = Tablero(id_jugador="juancho")
    print(tab1.inicializar_tablero())
    print("Tablero visible antes de los disparos:")
    print()
    print(tab1.tablero)
    coordenadas_disparos = [(0, 0), (2, 3), (5, 5)]
    for coordenada in coordenadas_disparos:
        fila, columna = coordenada
        impacto = tab1.disparo_coordenada(fila, columna)
        if impacto:
            print(f"¡Impacto en la coordenada {coordenada}!")
        else:
            print(f"Disparo en la coordenada {coordenada}, sin impacto.")

    # Mostrar el tablero después de los disparos
    # print("\n")
    print("Tablero visible después de los disparos:")
    print(tab1.tablero)
    print()
    print("Tablero oculto después de los disparos:")
    print(tab1.tablero_oculto)
    
   
    
    




