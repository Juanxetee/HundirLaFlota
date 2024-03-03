def disparo_coordenada(self, fila, columna):
        if self.tablero_oculto[fila, columna] == 1:
            self.tablero_oculto[fila, columna] = 2  # Cambia el estado del tablero oculto para mostrar el impacto
            self.tablero[fila, columna] = "X"  # Cambia el estado del tablero visible para mostrar el impacto
            return True
        else:
            self.tablero_oculto[fila, columna] = 3  # Cambia el estado del tablero oculto para mostrar el disparo del oponente
            self.tablero[fila, columna] = '~'
            return False    

# BONUS: RECOMPENSA creamos input de 1 o 2 para que el user elija una recompensa
def eleccionrecompensa(tablero):
    pregunta= (input("Elige 1 si quieres un nuevo tiro y Elige 2 si quieres reparar una pieza de barco"))
    if pregunta == 1:
        recibe_disparo(tablero)
    elif pregunta ==2:
        arreglabarco(tablero)
        cambioturno
    else:
        print("Has introducido un valor no válido pierdes la recompensa")
    return tablero

def recibe_disparo(tablero):
    #for disparo in tablero creamos un input de coordenada:
    control = False
    contador=0
    while not control:
        coordenadarecib = tuple(map(int,input("PC introduce la cooordenada").split(',')))
        if tablero[coordenadarecib]=="0": 
            tablero[coordenadarecib]="X"
            print(f" Tocado")
            print(tablero)
            control= False 
            contador=contador+1
            if contador==2:
                eleccionrecompensa(tablero)
                #print(f" Contador: {contador}")
                contador=0
                print(contador)
        elif tablero[coordenadarecib]=="X":
            print("Dispara a otro punto más tarde,ahora cambia de turno")
            control= True
        else:
            print(f"Agua, cambia de turno")
            control= True
    return tablero
    #else:
    #    print("Cambio de turno")

tablero=recibe_disparo(tablero)
print(tablero)
         