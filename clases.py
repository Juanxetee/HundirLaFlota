import numpy as np 
from variables import dimensiones, barcos # Importamos las variables desde variables.py
 
#Aquí definimos la clase Tablero, que representa el tablero de juego para un jugador. La clase tiene métodos para inicializar el tablero con los barcos y
# validar posiciones. Utiliza la biblioteca numpy para manejar matrices.

class Tablero:
    # Constructor de la clase Tablero
    def __init__(self, id_jugador):
        # Inicializa las propiedades del tablero
        self.id_jugador = id_jugador  # Identificador del jugador
        self.dimensiones = dimensiones  # Tamaño del tablero
        self.barcos = barcos  # Barcos a colocar en el tablero
        # Matrices para los tableros visibles y ocultos del jugador y la máquina
        self.tablero_visible_jugador = np.full((self.dimensiones, self.dimensiones), '~', dtype=str) # tablero donde el jugador ve sus disparos
        self.tablero_visible_maquina = np.full((self.dimensiones, self.dimensiones), '~', dtype=str) #tablero donde actua la maquina
        self.tablero_oculto_jugador = np.zeros((self.dimensiones, self.dimensiones), dtype=int) #tablero donde estan los barcos del jugador, el usuario lo ve
        self.tablero_oculto_maquina = np.zeros((self.dimensiones, self.dimensiones), dtype=int) # tablero oculto para el usuario donde estan los barcos de la maquina
        # Matrices para registrar los disparos realizados por el jugador y la máquina
        self.disparos_realizados_jugador = np.zeros((self.dimensiones, self.dimensiones), dtype=bool)
        self.disparos_realizados_maquina = np.zeros((self.dimensiones, self.dimensiones), dtype=bool)
        # Coloca los barcos en el tablero
        self.colocar_barcos()

    # Método para colocar los barcos en el tablero
    def colocar_barcos(self):
        for barco, longitud in self.barcos.items():
            colocado = False
            while not colocado:
                fila = np.random.randint(0, self.dimensiones)
                columna = np.random.randint(0, self.dimensiones)
                orientacion = np.random.choice(["H", "V"])
                # Verifica si la posición es válida para colocar el barco
                if self.validar_posicion(fila, columna, orientacion, longitud):
                    # Coloca el barco en la posición válida
                    if orientacion == "H":
                        if self.id_jugador == "Jugador":
                            self.tablero_oculto_jugador[fila, columna:columna + longitud] = 1
                        else:
                            self.tablero_oculto_maquina[fila, columna:columna + longitud] = 1
                    else:
                        if self.id_jugador == "Jugador":
                            self.tablero_oculto_jugador[fila:fila + longitud, columna] = 1
                        else:
                            self.tablero_oculto_maquina[fila:fila + longitud, columna] = 1
                    colocado = True

    # Método para validar si una posición es válida para colocar un barco
    def validar_posicion(self, fila, columna, orientacion, longitud):
        if orientacion == "H":
            if columna + longitud > self.dimensiones:
                return False
            if np.any(self.tablero_oculto_jugador[fila, columna:columna + longitud]) or np.any( #coge una fila del tablero oculto jugador y dada una columna hasta
                self.tablero_oculto_maquina[fila, columna:columna + longitud]): # las mismas columnas como longitud tenga el barco a colocar
                return False #si devuelve true signifca que hay un barco, por eso debe ser false, indicando que esta vacio
        else:
            if fila + longitud > self.dimensiones:
                return False
            if np.any(self.tablero_oculto_jugador[fila:fila + longitud, columna]) or np.any(
                    self.tablero_oculto_maquina[fila:fila + longitud, columna]):
                return False
        return True 

    # Método para registrar un disparo del jugador en una coordenada específica
    def disparo_coordenada_jugador(self, fila, columna):
        self.disparos_realizados_jugador[fila, columna] = True
        if self.tablero_oculto_maquina[fila, columna] == 1:
            self.tablero_oculto_maquina[fila, columna] = 2
            self.tablero_visible_jugador[fila, columna] = "X"  # Barco impactado
            return True
        else:
            self.tablero_visible_jugador[fila, columna] = "."  # Agua
            return False

    # Método para registrar un disparo de la máquina en una coordenada específica
    def disparo_coordenada_maquina(self, fila, columna):
        self.disparos_realizados_maquina[fila, columna] = True
        if self.tablero_oculto_jugador[fila, columna] == 1:
            self.tablero_oculto_jugador[fila, columna] = 2
            self.tablero_visible_jugador[fila, columna] = "X"  # Barco impactado
            return True
        else:
            self.tablero_visible_maquina[fila, columna] = "."  # Agua
            return False

    # Método para mostrar en pantalla el tablero del jugador
    def mostrar_tablero_jugador(self):
        print("   " + " ".join([str(i) for i in range(self.dimensiones)]))
        for i in range(self.dimensiones):
            fila = ""
            for j in range(self.dimensiones):
                if self.tablero_visible_jugador[i, j] == "~":
                    if self.tablero_oculto_jugador[i, j] == 1:
                        fila += "O "  # Barco oculto
                    else:
                        fila += "~ "  # Agua oculta
                else:
                    fila += self.tablero_visible_jugador[i, j] + " "  # Barco impactado o agua visible
            print(f"{i}  {fila}")

    # Método para mostrar en pantalla el tablero de la máquina (solo con los disparos del jugador visibles)
    def mostrar_tablero_maquina(self):
        print("   " + " ".join([str(i) for i in range(self.dimensiones)]))
        for i in range(self.dimensiones):
            fila = ""
            for j in range(self.dimensiones):
                if self.tablero_visible_maquina[i, j] == "~":
                    if self.tablero_oculto_maquina[i, j] == 1:
                        fila += "O "  # Barco oculto
                    else:
                        fila += "~ "  # Agua oculta
                else:
                    fila += self.tablero_visible_maquina[i, j] + " "  # Barco impactado o agua visible
            print(f"{i}  {fila}")

# if __name__ == "__main__": 
#     tab1 = Tablero(id_jugador="juancho")
#     print(tab1.inicializar_tablero())
#     print("Tablero visible antes de los disparos:")
#     print()
#     print(tab1.tablero)
#     coordenadas_disparos = [(0, 0), (2, 3), (5, 5)]
#     for coordenada in coordenadas_disparos:
#         fila, columna = coordenada
#         impacto = tab1.disparo_coordenada(fila, columna)
#         if impacto:
#             print(f"¡Impacto en la coordenada {coordenada}!")
#         else:
#             print(f"Disparo en la coordenada {coordenada}, sin impacto.")

#     # Mostrar el tablero después de los disparos
#     # print("\n")
#     print("Tablero visible después de los disparos:")
#     print(tab1.tablero)
#     print()
#     print("Tablero oculto después de los disparos:")
#     # print(tab1.tablero_oculto)
    
   
    
    




