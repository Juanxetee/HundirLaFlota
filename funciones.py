#Importamos de hoja variables y clases los correspondientes objetos
from variables import barcos, dimensiones
from clases import Tablero

import numpy as np

#Creamos función obtener_coordenadas: que pide al jugador introducir las coordenadas donde desea realizar su disparo. 
#El bucle while True asegura que la función seguirá pidiendo coordenadas hasta que se introduzcan valores válidos. Que sean válidas depende 
#de que estén dentro del rango permitido (en este caso, entre 0 y 9) y quepa en el tablero (determinado por la variable dimensiones)
# Si el valor está fuera de rango o no es numérico, se captura el error y se pide al usuario que reintente.

def obtener_coordenadas():
    while True:
        try:
            fila = int(input("Introduce la fila (0-9): "))
            columna = int(input("Introduce la columna (0-9): "))
            if 0 <= fila < dimensiones and 0 <= columna < dimensiones:
                return fila, columna
            else:
                print("Coordenadas fuera de rango. Inténtalo de nuevo.")
        except ValueError: #lo incluimos por si el jugador mete valores no numericos
            print("Por favor, introduce valores numéricos válidos.")

# Función para el turno del jugador
#Creamos la función turno_jugador: que gestiona el turno del jugador humano. Recibe como argumentos el tablero de juego y las coordenadas (fila y columna)
# donde el jugador desea disparar. Llama a la función disparo_coordenada_jugador que realiza el disparo en el tablero del oponente 
#y devuelve un valor booleano indicando si se impactó un barco , si lo hace -True- sigue jugando al pedir nuevas coordenadas, si no acierta -False-  termina 
#el turno del jugador. Después de cada disparo, se muestra el tablero actualizado y se notifica al jugador el resultado de su acción. 

def turno_jugador(tablero, fila, columna):
    while True:
        impacto = tablero.disparo_coordenada_jugador(fila, columna)
        tablero.mostrar_tablero_jugador()
        if impacto:
            print("¡Has impactado en un barco!")
            fila, columna = obtener_coordenadas()  # Vuelve a pedir coordenadas
        else:
            print("Agua...")
            break  # Si no hay impacto en un barco, el turno del jugador termina

# Función para el turno de la máquina
def turno_maquina(tablero_visible_maquina):
# Creamos función turno_maquina: que gestiona el turno de la máquina. Selecciona aleatoriamente las coordenadas de disparo utilizando np.random.randint, válido
# ya que se ha importando la biblioteca NumPy al principio del código. Se llama a una función (disparo_coordenada_maquina) que realiza el disparo y 
#devuelve si hubo un impacto o no. Después de cada disparo, se notifica el resultado. Si la máquina impacta, puede seguir disparando y si falla, su turno termina.

def turno_maquina(tablero_jugador, tablero_maquina):
    while True:
        fila = np.random.randint(0, tablero_jugador.dimensiones)
        columna = np.random.randint(0, tablero_jugador.dimensiones)
        impacto = tablero_jugador.disparo_coordenada_jugador(fila, columna)  # Cambio aquí
        #María FM: aquí ver si mostrar tablero como en línea 32.
        fila = np.random.randint(0, tablero_visible_maquina.dimensiones)
        columna = np.random.randint(0, tablero_visible_maquina.dimensiones)
        impacto = tablero_visible_maquina.disparo_coordenada_maquina(fila, columna)  
        print(f"La máquina dispara en la fila {fila} y columna {columna}")
        if impacto:
            print("¡La máquina ha impactado en uno de tus barcos!")
        else:
            print("La máquina ha dado en el agua...")
            break

# Función para verificar si el juego ha terminado
# Creamos la función juego_terminado: que determina si el juego ha terminado. Comprueba si alguno de los tableros (del jugador o de la máquina)
# no tiene más barcos, es decir, si la suma de los valores en el tablero oculto es 0. 
#El "tablero oculto" es una representación del tablero donde los barcos no impactados se marcan con un valor (por ejemplo, 1) 
#y los impactados o el agua con otro (por ejemplo, 0). Si alguno de los tableros está completamente vacío, la función devuelve True, 
#indicando que el juego ha terminado
def juego_terminado(tablero_jugador, tablero_maquina):
    return np.sum(tablero_jugador.tablero_oculto_jugador == 1) == 0 or np.sum(tablero_maquina.tablero_oculto_maquina == 1) == 0