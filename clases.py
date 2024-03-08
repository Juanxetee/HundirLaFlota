import numpy as np 
from variables import dimensiones, barcos # Importamos las variables desde variables.py
 
#Aquí definimos la clase Tablero, que representa el tablero de juego para un jugador. La clase tiene métodos para inicializar el tablero con los barcos y
# validar posiciones. Utiliza la biblioteca numpy para manejar matrices.

class Tablero:
    #Tenemos un constructor que inicializa las propiedades del tablero, id del jugador, las dimensiones del tablero, los barcos y dos matrices numpy: tablero visible y tablero oculto.
    def __init__(self, id_jugador):
        self.id_jugador = id_jugador
        self.dimensiones = dimensiones
        self.barcos = barcos
        self.tablero_visible_jugador = np.full((self.dimensiones, self.dimensiones), '~', dtype=str)
        self.tablero_visible_maquina = np.full((self.dimensiones, self.dimensiones), '~', dtype=str)
        self.tablero_oculto_jugador = np.zeros((self.dimensiones, self.dimensiones), dtype=int)
        self.tablero_oculto_maquina = np.zeros((self.dimensiones, self.dimensiones), dtype=int)
        self.disparos_realizados_jugador = np.zeros((self.dimensiones, self.dimensiones), dtype=bool)
        self.disparos_realizados_maquina = np.zeros((self.dimensiones, self.dimensiones), dtype=bool)
        self.colocar_barcos()

#Se crea la función colocar_barcos que permite colocar barcos en tableros (están en variables). Primero itera sobre diccionario barcos, que contiene los tipos de barcos 
#como claves y las longitudes como valores.  Para cada tipo de barco, se ejecuta un bucle while hasta que el barco se coloque correctamente. Se generan aleatoriamente coordenadas
#dentro del tablero (self.dimensiones). También se elige aleatoriamente una orientación ("H" para horizontal y "V" para vertical). Llama a la función validar_posicion, que se explica
#en el siguiente bloque. Con ella, verifica si la posición generada aleatoriamente es válida para colocar el barco. Siendo válida, coloca en el tablero oculto: Si la posición es válida,
#se coloca el barco en el tablero oculto (self.tablero_oculto_jugador o self.tablero_oculto_maquina, dependiendo del turno) con valor igual a 1 en la coordenada valida. 
#Una vez que el barco se ha colocado, la variable colocado es True, lo que hace que el bucle while termine y se pase al siguiente barco en el diccionario. 
        
    def colocar_barcos(self):
        for barco, longitud in self.barcos.items():
            colocado = False
            while not colocado:
                fila = np.random.randint(0, self.dimensiones)
                columna = np.random.randint(0, self.dimensiones)
                orientacion = np.random.choice(["H", "V"])

                if self.validar_posicion(fila, columna, orientacion, longitud):
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

    def validar_posicion(self, fila, columna, orientacion, longitud):
        if orientacion == "H":
            if columna + longitud > self.dimensiones:
                return False
            if np.any(self.tablero_oculto_jugador[fila, columna:columna + longitud]) or np.any(self.tablero_oculto_maquina[fila, columna:columna + longitud]):
                return False
        else:
            if fila + longitud > self.dimensiones:
                return False
            if np.any(self.tablero_oculto_jugador[fila:fila + longitud, columna]) or np.any(self.tablero_oculto_maquina[fila:fila + longitud, columna]):
                return False
        return True

    def disparo_coordenada_jugador(self, fila, columna):
        self.disparos_realizados_jugador[fila, columna] = True
        if self.tablero_oculto_maquina[fila, columna] == 1:
            self.tablero_oculto_maquina[fila, columna] = 2
            self.tablero_visible_jugador[fila, columna] = "X"
            return True
        else:
            self.tablero_visible_jugador[fila, columna] = "."
            return False

    def disparo_coordenada_maquina(self, fila, columna):
        self.disparos_realizados_maquina[fila, columna] = True
        if self.tablero_oculto_jugador[fila, columna] == 1:
            self.tablero_oculto_jugador[fila, columna] = 2
            self.tablero_visible_maquina[fila, columna] = "X"
            return True
        else:
            self.tablero_visible_maquina[fila, columna] = "."
            return False

    def mostrar_tablero_jugador(self):
        print("   " + " ".join([str(i) for i in range(self.dimensiones)]))
        for i in range(self.dimensiones):
            fila = ""
            for j in range(self.dimensiones):
                if self.tablero_visible_jugador[i, j] == "~":
                    if self.tablero_oculto_jugador[i, j] == 1:
                        fila += "O "
                    else:
                        fila += "~ "
                else:
                    fila += self.tablero_visible_jugador[i, j] + " "
            print(f"{i}  {fila}")

    def mostrar_tablero_maquina(self):
        print("   " + " ".join([str(i) for i in range(self.dimensiones)]))
        for i in range(self.dimensiones):
            fila = ""
            for j in range(self.dimensiones):
                if self.tablero_visible_maquina[i, j] == "~":
                    if self.tablero_oculto_maquina[i, j] == 1:
                        fila += "O "
                    else:
                        fila += "~ "
                else:
                    fila += self.tablero_visible_maquina[i, j] + " "
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
    
   
    
    




