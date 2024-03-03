import numpy as np
import random
#crear tablero: como variable
#clrtablero=np(10,10," ")
#print(tablero)
#como nos hace falta la función crear tablero mejor no crear la variable si no la función (con tablero dentro)
def crea_tablero(lado=10):
    tablero=np.full((lado,lado)," " )
    return tablero  

tablerouser= crea_tablero(10)

def crea_tableropc(lado=10):
    tableropc=np.full((lado,lado)," " )
    return tableropc  
tableropc= crea_tableropc(10)
tablero_oculto=tableropc.copy()
#print(tablero_oculto)

# Crear variable barco y funcion Colocar barco: Posiciona un par de barcos en [(0,1), (1,1)] y [(1,3), (1,4), (1,5), (1,6)]./
# Los barcos serán Os mayúsculas. Como ves, un barco de dos posiciones de eslora y otro de cuatro.
#primero creamos barco 1
barco1= [(0,1),(1,1)]
barco2= [(1,3),(1,4),(1,5),(1,6)]
#crear función Colocar barco:
def coloca_barco(tablero,barco):
    for pieza in barco:
        tablero[pieza]="0"
    return tablero

#paso función colocar barco sobre tablero jugador
for barco in [barco1,barco2]:
    tablerouser = coloca_barco(tablerouser,barco)
#print("Tablero jugador")
#print(tablerouser)

barco1pc= [(1,4),(1,5)]
barco2pc= [(3,1),(4,1),(5,1),(6,1)]

#paso función colocar barco sobre tablero pc
for barco in [barco1pc,barco2pc]:
    tableropc = coloca_barco(tableropc,barco)
#print("Tablero pc")
#print(tableropc)
tablero_tamaño=10
#print("turno jugador")

'''
#defino función para barco hundido en tablero pc
def barcohundido(tablero,barco,coordenada):
    for barco in barco1pc,barco2pc:
        for pieza in barco:
            if pieza==coordenada:
                for pieza in barco:
                    if tableropc[pieza] == "0":
                        print("Barco tocado pero no hundido,sigue intentando")
                        return
                print("Barco hundido")

'''
def finpartidapc(tableropc):
    suma=0
    vidas=len(barco1pc)+ len(barco2pc)
    for fila in tableropc:
        for celda in fila:
            if celda=="X":
                suma +=1
                if vidas==suma:
                    print("final de la partida, has ganado")
    return

def finpartidajug(tablero):
    suma=0
    vidas=len(barco1)+ len(barco2)
    for fila in tablerouser:
        for celda in fila:
            if celda=="X":
                suma +=1
            if vidas==suma:
                print("final de la partida, ha ganado PC")
    return


def disparar(tablero,tablero_oculto):
    fallo_jugador= False
    finpartidajug= False
    #control = False
    #contador=0

    while not finpartidajug:
        while not fallo_jugador:
            try: 
            #Creamos solicitud de coordenadas y revisamos que sean validas en el tablero
                entrada = input("Jugador, por favor introduce la coordenada (ej. 3,4): ")
                coordenada_x, coordenada_y = map(int, entrada.split(','))      
                
                if 0 <= coordenada_x < tablero_tamaño and 0 <= coordenada_y < tablero_tamaño:
                    coordenada = (coordenada_x, coordenada_y)
            
                    tablero= tableropc
                    tablero_oculto1= tablero_oculto
                    if tablero[coordenada]=="0": 
                        tablero[coordenada]="X"
                        print(f" Tocado vuelve a disparar")
                        tablero_oculto1[coordenada]="X"
                        print(tablero_oculto1)

                    #control= False
                        fallo_jugador= False
                    #contador=contador+1
                    #if contador==2:
                    #    tablero= tablerouser
                    #    recompensa(tablero)
                        #print(f" Contador: {contador}")
                    #    contador=0
                    #   print(contador)
                        #barcohundido(tablero,barco,coordenada)
                    elif tablero[coordenada]=="X":
                        print("Dispara a otro punto más tarde,ahora cambia de turno")
                        fallo_jugador= True
                    else:
                        print(f"Agua, cambia de turno")
                        fallo_jugador= True
                        return tablero
                else: print("Coordenada fuera de rango, vuelve a intentarlo")
            except ValueError:
                print("No es una coordenada válida, por favor introduce una coordenada de nuevo")   
    return tablero
        #else:

#funcion disparo PC a tablero jugador
def disparopc(tablero):
    print("aqui")
    fallo_jugador= True
    finpartidapc= False   
    while not finpartidapc:
        #fallo_jugador= True
        while fallo_jugador:
            try: 
            #Creamos solicitud de coordenadas y revisamos que sean validas en el tablero
                entrada = input("PC, por favor introduce la coordenada (ej. 3,4): ")
                coordenada_x, coordenada_y = map(int, entrada.split(','))      
                
                if 0 <= coordenada_x < tablero_tamaño and 0 <= coordenada_y < tablero_tamaño:
                    coordenada = (coordenada_x, coordenada_y)
            
                    tablero= tablero
                    if tablero[coordenada]=="0": 
                        tablero[coordenada]="X"
                        print(f" Tocado vuelve a disparar")
                        print(tablero)
                        fallo_jugador= True
                        #barcohundido(tablero,barco,coordenada)
                    elif tablero[coordenada]=="X":
                        print(" Disparo de PC ha fallado,ahora toca cambio de turno")
                        fallo_jugador= False
                    else:
                        print(f"Agua, cambia de turno")
                        fallo_jugador= False
                else: print("Coordenada fuera de rango, vuelve a intentarlo")
            except ValueError:
                print("No es una coordenada válida, por favor introduce una coordenada de nuevo")   
    return tablero
    #else:
tablero=disparar(tableropc,tablero_oculto)
print("aqui")

tablerouser=disparopc(tablerouser)

finpartidapc(tableropc)

finpartidajug(tablerouser)

       