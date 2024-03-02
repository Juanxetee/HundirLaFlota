# Función que crea el tablero
def crear_tablero(largo,ancho):
    tablero = np.full((largo,ancho), " ")
    return tablero
    
tablero_resultante = crear_tablero(10,10)
print(tablero_resultante)
