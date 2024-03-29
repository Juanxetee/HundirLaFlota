import numpy as np

# Variables
dimensiones_tablero = 10
barcos = {
    "Barco1":1,
    "Barco2":2,
    "Barco3":3,
    "Barco4":4
}

diccionario_coord_jugador = {} # Pendiente si al final lo utilizamos o no
diccionario_coord_ordenador = {} # Pendiente si al final lo utilizamos o no
coord_disparo_ordenador = []
coord_disparo_jugador = []
vidas_usuario = sum(barcos.values())
vidas_ordenador = sum(barcos.values())

# Clase
class Tablero:
#Tenemos un constructor que inicializa las propiedades del tablero, id del jugador, las dimensiones del tablero, los barcos y dos matrices numpy: tablero visible y tablero oculto.
    def __init__(self, id_jugador):
        self.id_jugador = id_jugador
        self.dimensiones = dimensiones_tablero
        self.barcos = barcos
        self.tablero_barcos_usuario = np.full((self.dimensiones, self.dimensiones), " ")  
        self.tablero_ordenador = np.full((self.dimensiones, self.dimensiones), " ")   
        self.tablero_juego_usuario = np.full((self.dimensiones, self.dimensiones), " ")
       

    
    # Funciones        
    def inicializar_tablero_usuario(self):
        # Colocar los barcos en el tablero oculto
        for barco, longitud in self.barcos.items(): #bucle for para iterar sobre los barcos definidos en variables
            colocado = False
            while not colocado: #genera aleatoriamente una fila y columna de inicio, así como una orientación, seguira en bucle hasta colocar
                fila = np.random.randint(0, self.dimensiones)
                columna = np.random.randint(0, self.dimensiones)
                orientacion = np.random.choice(["N","S","O","E"])

                if self.validar_posicion(fila, columna, orientacion, longitud,self.tablero_barcos_usuario):
                    coordenadas=[]
                    if orientacion == 'N':
                        for i in range(longitud):
                            #MF: Ver si en vez de ="O"  es igual a 0 ya que el tablero se ha llenado con np.zeros, igual en los otros puntos cardinales.
                            self.tablero_barcos_usuario[fila - i, columna] = "O"
                            coordenadas.append((fila - i, columna))
                    elif orientacion == 'S':
                        for i in range(longitud):
                            self.tablero_barcos_usuario[fila + i, columna] = "O"
                            coordenadas.append((fila - i, columna))
                    elif orientacion == 'O':
                        for i in range(longitud):
                            self.tablero_barcos_usuario[fila, columna - i] = "O"
                            coordenadas.append((fila - i, columna))
                    elif orientacion == 'E':
                        for i in range(longitud):
                            self.tablero_barcos_usuario[fila, columna + i] = "O"
                            coordenadas.append((fila - i, columna))
                    diccionario_coord_jugador[barco]=coordenadas
                    colocado = True #verifica si la posición es válida utilizando el método validar_posicion, si es válida, coloca el barco en el tablero propio


    def inicializar_tablero_ordenador(self):
        # Colocar los barcos en el tablero oculto
        for barco, longitud in self.barcos.items(): #bucle for para iterar sobre los barcos definidos en variables
            colocado = False
            while not colocado: #genera aleatoriamente una fila y columna de inicio, así como una orientación, seguira en bucle hasta colocar
                fila = np.random.randint(0, self.dimensiones)
                columna = np.random.randint(0, self.dimensiones)
                orientacion = np.random.choice(["N","S","O","E"])

                if self.validar_posicion(fila, columna, orientacion, longitud,self.tablero_ordenador):
                    coordenadas=[]
                    if orientacion == 'N':
                        for i in range(longitud):
                            #MF: Ver si en vez de ="O"  es igual a 0 ya que el tablero se ha llenado con np.zeros, igual en los otros puntos cardinales.
                            self.tablero_ordenador[fila - i, columna] = "O"
                            coordenadas.append((fila - i, columna))
                    elif orientacion == 'S':
                        for i in range(longitud):
                            self.tablero_ordenador[fila + i, columna] = "O"
                            coordenadas.append((fila - i, columna))
                    elif orientacion == 'O':
                        for i in range(longitud):
                            self.tablero_ordenador[fila, columna - i] = "O"
                            coordenadas.append((fila - i, columna))
                    elif orientacion == 'E':
                        for i in range(longitud):
                            self.tablero_ordenador[fila, columna + i] = "O"
                            coordenadas.append((fila - i, columna))
                    diccionario_coord_ordenador[barco]=coordenadas
                    colocado = True #verifica si la posición es válida utilizando el método validar_posicion, si es válida, coloca el barco en el tablero propio
                    
                    
    def validar_posicion(self, fila, columna, orientacion, longitud, tablero):
        print(longitud)
        print("validando posicion")
        if orientacion == 'N':
            if fila - longitud + 1 < 0:
                return False
            for i in range(longitud):
                if tablero[fila - i, columna] != '~':
                    return False
        elif orientacion == 'S':
            if fila + longitud > self.dimensiones:
                return False
            for i in range(longitud):
                if tablero[fila + i, columna] != '~':
                    return False
        elif orientacion == 'O':
            if columna - longitud + 1 < 0:
                return False
            for i in range(longitud):
                if tablero[fila, columna - i] != '~':
                    return False
        elif orientacion == 'E':
            if columna + longitud > self.dimensiones:
                return False
            for i in range(longitud):
                if tablero[fila, columna + i] != '~':
                    return False
        print("Termina validacion")
        return True  
    
    
    
# Esto es una prueba de los tableros y coordenadas    
# tab1 = Tablero(id_jugador="Jugador")
# tab1.inicializar_tablero_usuario()
# tab1.inicializar_tablero_ordenador()

# print(tab1.tablero_ordenador)
# print(diccionario_coord_ordenador)
# print()
# print(tab1.tablero_barcos_usuario)
# print(diccionario_coord_jugador)
# print()
# print(tab1.tablero_juego_usuario)             




    # Esta función une tanto la función de disparo del usuario, como la del ordenador y pone fin a la partida
    def juego(self,vidas_usuario,vidas_ordenador):
        while vidas_usuario > 0 and vidas_ordenador >0:
            self.disparo_jugador(vidas_ordenador)
            if vidas_ordenador <= 0:
                print("¡Has ganado!")
                break
            self.disparo_ordenador(vidas_usuario)
            if vidas_usuario <= 0:
                print("¡Ha ganado el ordenador!")
                break    
    
        

    # Esta función lleva la dinámica de disparos del jugador
    def disparo_jugador(self):
        pregunta = "\nIntroduce aquí las coordenadas de disparo (ej. 3,4): \n"
        pregunta += "\nEscribe 'fin' para salir del programa"
        
        entrada = ""
        while entrada != "fin":
            
            fallo_jugador = False
            while not fallo_jugador:

                # Solicitamos al jugador que introduzca sus coordenadas    
                entrada = input(pregunta)
                fila, columna = map(int, entrada.split(','))
                coord_disparo= (fila,columna)
                # Comprobamos que las coordenadas sean válidas para el tablero
                if 0 <= fila < dimensiones_tablero and 0 <= columna < dimensiones_tablero:
                    # Si ha tocado barco
                    if self.tablero_ordenador[fila][columna]== "O":
                        self.tablero_juego_usuario[fila][columna] = "X"
                        self.tablero_ordenador[fila][columna]= "X"
                        coord_disparo_jugador.append(coord_disparo)
                        print("Tocado, puedes volver a disparar")
                        print("Así queda tu tablero de disparos \n",self.tablero_juego_usuario)
                        print()
                        vida_ordenador -=1


                    # Si es agua    
                    elif self.tablero_ordenador[fila][columna]== " ":
                        self.tablero_juego_usuario[fila][columna] = "~"
                        self.tablero_ordenador[fila][columna]= "~"
                        coord_disparo_jugador.append(coord_disparo)
                        print("Agua, pierdes turno")
                        print("Así queda tu tablero de disparos \n",self.tablero_juego_usuario)
                        fallo_jugador = True

                    # Si ya está dicha    
                    else:
                        if self.tablero_ordenador[fila][columna] == "X" or self.tablero_ordenador[fila][columna] == "~":
                            print("Esa coordenada ya estaba dicha. Pierdes turno")
                            fallo_jugador = True
                else:
                    print("Las coordenadas que has dado no son válidas. Pierdes turno")
                    fallo_jugador = True
            

    def disparo_ordenador(self):
            repetido = True
            while repetido:
                fila = np.random.randint(0, self.dimensiones)
                columna = np.random.randint(0, self.dimensiones)
                coord_disparo = (fila,columna)
                
                if coord_disparo not in coord_disparo_ordenador:
                    if self.tablero_barcos_usuario[fila][columna]== "O":
                        self.tablero_barcos_usuario[fila][columna]= "X"
                        self.tablero_ordenador[fila][columna]= "X"
                        vida_usuario -=1
                        print("Tocado, vuelvo a disparar")
                        print("Así queda tu tablero de juego \n",self.tablero_barcos_usuario)
                        coord_disparo_ordenador.append(coord_disparo)
                        vidas_usuario -=1
                
                    
                # Si es agua    
                    else:
                        self.tablero_barcos_usuario[fila][columna]== " "
                        self.tablero_barcos_usuario[fila][columna] = "~"
                        self.tablero_ordenador[fila][columna]= "~"
                        print("Agua. Te toca a tí")
                        print("Así queda tu tablero de juego \n",self.tablero_barcos_usuario)
                        coord_disparo_ordenador.append(coord_disparo)
                        repetido = False

def mostrar_tablero(tablero):
    print("   0 1 2 3 4 5 6 7 8 9")
    for i in range(len(tablero)):
        print(i, end="  ")
        for j in range(len(tablero[i])):
            if tablero[i, j] == 0:
                print(".", end=" ")
            elif tablero[i, j] == 1:
                print("O", end=" ")
            elif tablero[i, j] == 2:
                print("X", end=" ")
        print()

def main():
    print("inicializa vidas usuario y ordenador")
    vidas_usuario = sum(barcos.values())
    vidas_ordenador = sum(barcos.values())
    print("tablero jugador")
    tablero_jugador = Tablero("Jugador")
    print("tablero ordenador")
    tablero_ordenador = Tablero("Ordenador")
    print("init tab us")
    tablero_jugador.inicializar_tablero_usuario()
    print("init tab ord")
    tablero_ordenador.inicializar_tablero_ordenador()

    print("¡Bienvenido a Batalla Naval!\n")
    print("Instrucciones:")
    print(" - 'O' representa un barco")
    print(" - 'X' representa un barco impactado")
    print(" - '~' representa agua\n")

    while True:
        # Turno del jugador
        print("Tu turno:")
        tablero_ordenador.mostrar_tablero()
        tablero_jugador.disparo_jugador()
        if vidas_ordenador <= 0:
            print("¡Has ganado!")
            break

        # Turno del ordenador
        print("\nTurno del Ordenador:")
        tablero_jugador.disparo_ordenador()
        if vidas_usuario <= 0:
            print("¡El Ordenador ha ganado!")
            break

if __name__ == "__main__":
    main()     
