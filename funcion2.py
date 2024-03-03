def disparo_coordenada(self, fila, columna):
        if self.tablero_oculto[fila, columna] == 1:
            self.tablero_oculto[fila, columna] = 2  # Cambia el estado del tablero oculto para mostrar el impacto
            self.tablero[fila, columna] = "X"  # Cambia el estado del tablero visible para mostrar el impacto
            return True
        else:
            self.tablero_oculto[fila, columna] = 3  # Cambia el estado del tablero oculto para mostrar el disparo del oponente
            self.tablero[fila, columna] = '~'
            return False    

# BONUS: RECOMPENSA creamos recompensa de reparar una pieza
def recompensa(tablero):
    pregunta= (input("Si quieres reparar una pieza de barco pulsa 1"))
    if pregunta ==1:
        arreglabarco(tablero)
        disparar(tablero)
    else:
        print("Has introducido un valor no válido pierdes la recompensa")
    return tablero

def disparar(tablero):
    #for disparo in tablero creamos un input de coordenada:
    fallo_jugador= False
    control = False
    contador=0
    while not control:
        coordenada = tuple(map(int,input("Jugador por favor introduce la cooordenada").split(',')))
        tablero= self.tableropc
        tablerooculto= self.tablero_oculto
        if tablero[coordenada]=="0": 
            tablero[coordenada]="X"
            print(f" Tocado vuelve a disparar")
            tablerooculto[coordenada]="X"
            print(tablero_oculto)
            control= False
            fallo_jugador= False
            contador=contador+1
            if contador==2:
                recompensa(tablero)
                #print(f" Contador: {contador}")
                contador=0
                print(contador)
        elif tablero[coordenada]=="X":
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


#verificar que coordenada es válida para el tablero


#función elegir paso para el usuario (bonus)
def elegiropcion():
    pregunta= (int(input("Elige 1 si quieres disparar. / Elige 2 si quieres ver tu tablero. / Elige 3 si quieres ver tus disparos en el tablero de tu contrincante / Elige 4 si quieres salir")))
    if pregunta == 1:
        crear_disparo(tablero)
    elif pregunta ==2:
        mostrartablero(tablero)
    elif pregunta ==3:
        mostrartablerouser2(tablerouser2)
   else:
        print("Has introducido un valor no válido")
    return tablero


    




         