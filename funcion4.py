

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