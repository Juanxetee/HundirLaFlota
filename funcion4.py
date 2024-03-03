# Notas Marce

# Lo de inicializar el tablero (que primero debe estar vacío) para poblarlo con barcos, ¿no son 2 pasos diferentes (1: crear 2: poblar)?
# por qué los barcos ya están dentro de la clase Tablero?

# En clases no hay que inicializar un tercer tablero?
tab0 = Tablero() # sería el tablero vacío que se genera al inicializar la clase tablero, no?
tab1 = Tablero(id_jugador="juancho") # Los barcos de jugador 1
tab2 = Tablero(id_jugador="juancho") # Los disparos de jugador 1. ¿Iría con mismo id_jugador???


# En las instrucciones se recomienda crear una clase barcos. 
# No se me ocurre qué atributos pueden tener más allá de la eslora...

class Barco:
# Aquí definiríamos los atributos y métodos de la clase barcos
    def __init__(self, eslora):
        self.eslora = eslora

# Dónde se definen las vidas, que son los números de casilleros totales de los barcos?
# No hay que, al inicializar el juego, incluir el parámetro "vidas" paracada jugador, que se rellene luego según los barcos?
# Y no se pone allí mismo que son 2 jugadores, por ej: id_jugador1 e id_jugador2, 
# y que al iniciar se le pregunte al jugador humano su nombre y con eso reemplace el "id_jugador1"?
vidas = [0]
for barco in barcos:
    vidas += eslora(barco)

# Poner los barcos en el tablero
def coloca_barcos(tablero, barcos):
    for barco in barcos:
        for c in barco:
            tablero[c] = "\U0001F6A2" # Unicode de "ship"

barcos = [[],[]] # Esto sellena con una lista por barco, que a su vez tiene las tuplas de las coordenadas de cada casillero
coloca_barcos(tab1, barcos) # Entiendo que le damos el parámetro del tablero del jugador
print(tab1)

# Disparar
def disparar(tablero, coordenada):
    if tablero[coordenada] == " ":
        print("Allí solo hay agua")
        tablero[coordenada] == "\U0001F30A" # Unicode de ola    
    elif tablero[coordenada] == "O":
        print("¡Le has dado!")
        tablero[coordenada] == "\U0001F525" # Unicode de fuego
        vidas -= 1  # Cada vez que se acierta un casillero de barco, se resta una vida
        while tablero[coordenada] == "O":
            disparar() #hay que poner un break o pass o algo para cuando el while se corta?
    else:
        pass 
# No me queda claro qué opción sería else, ya que o hay barco o hay agua... 
# a menos que sea una coordenada de fuera del tablero y haya que dar un mensaje de error, no solo pass...
# igual hay que definir que si es el jugador1 y acierta, la vida se le descuente al 2 y viceversa
# igualmente con los tableros, que si juega el jugador1, es en el tablero "oculto" que se refleja el acierto o errada, y viceversa

disparar(tab1,())
print(tablero) # va la tupla con las coordenadas

# Validar barco
def validar_barco(tablero, barco):
    ancho, largo = barco["Coordenadas"]
    eslora = barco["Eslora"]
    o = barco["Orientacion"]

    valido = True # a menos que se demuestre lo contrario

    if o == "N":
        for x in range(eslora):
            if not verificar_coord(tablero, ancho,largo+x+1):
                valido = False
                break
    elif o == "S":
        for x in range(eslora):
            if not verificar_coord(tablero, ancho,largo-x-1):
                valido = False
                break
    elif o == "E":
        for x in range(eslora):
            if not verificar_coord(tablero, ancho+x+1,largo):
                valido = False
                break
    else:
        for x in range(eslora):
            if not verificar_coord(tablero, ancho-x-1,largo):
                valido = False
                break
    return valido

def verificar_coord(tablero, ancho,largo):
    if ancho < 0 or ancho >= len(tablero):
        return False
    if largo < 0 or largo >= len(tablero):
        return False
    if tablero[ancho][largo] == "\U0001F6A2" or tablero[ancho][largo] == "\U0001F525": 
        return False
    return True

# Creación de los barcos aleatorios
eslora = x
# esto habría que adaptarlo para que haga uno diferente por cada tipo de barco (de 1,2,3 y 4 posiciones), pero dudo que se haga así
def barco_aleatorio(dimension):
    ancho = random.randint(0,dimension-1)
    largo = random.randint(0,dimension-1)
    o = random.choice("N","S","E","O")
    return ancho, largo, o

# Creación de las coordenadas aleatorias de los barcos:
def generar_coord(barco):
    ancho,largo = barco["Coordenadas"] 
    eslora = barco["Eslora"]
    o = barco["Orientacion"]

    coordenadas = [(ancho, largo)] 
    if o == "O":
        for x in range(eslora-1):
            coordenadas.append((ancho, largo-x-1))
    elif o == "E":
        for x in range(eslora-1):
            coordenadas.append((ancho, largo+x+1))
    elif o == "N":
        for x in range(eslora-1):
            coordenadas.append((ancho+x+1, largo))
    else:
        for x in range(eslora-1):
            coordenadas.append((ancho-x-1, largo))

def comprobar_coord(tablero, coordenadas):
    valida = True
    for ancho, largo in coordenadas:
        if ancho < 0 or ancho > len(tablero)-1 or largo < o or largo > len(tablero)-1:
            print("El barco debe caber dentro de las dimensiones del tablero")
            valida = False
            break
        if tablero[ancho][largo] == "\U0001F6A2" or tablero[ancho][largo] == "\U0001F525":
            print("Allí ya había otro barco")
            valida = False
            break
    return valida

def posicionar_barco(tablero, eslora):
    posicionado = False
    while not posicionado:
        ancho, largo, o = barco_aleatorio(len(tablero))
        print(f"Barco generado. Probando las coordenadas propuestas:{ancho}{largo}, eslora{eslora} y orientacion{0}")
        barco = {"Coordenadas": (ancho, largo), "Eslora":eslora, "Orientacion":o}
        coordenadas_barco = generar_coord(barco)
        print(f"Las coordenadas del barco son:{coordenadas_barco}")

        if verificar_coord(tablero,coordenadas_barco):
            posicionado = True
            print("Barco colocado")
    
    return coordenadas_barco


# Y esto ya parecería ser el juego:
# con esto se define el punto de partida, la coordenada inicial más la orientación
ancho, largo, o = barco_aleatorio(len(tablero))
print(f"Tentativa de barco. Posición inicial: [{ancho}][{largo}], y orientación: {o}")

# En este siguiente paso se generan las coordenadas, una para cada casillero (eslora) del barco
eslora = x 
# ¿Puede ser quehaya que hacer un bucle for que recorra la flota entera, cada barco con su eslora, 
# para que genere un barco aleatorio por cada elemento de la flora con su tamaño correspondiente?
barco={"Coordenadas":(ancho, largo), "Eslora": eslora, "Orientación":o}
coordenadas = generar_coord(barco)
print(coordenadas)

# Aquí se comprueba que esas ubicaciones sean válidas y ya se imprime el barco en el tablero
print(tablero)
comprobar_coord(tablero, coordenadas)

# Eso es para los barcos subsiguientes? Busca nuevas posibles posiciones para los nuevos barcos
# Pero de dónde saca cuántos barcos y de qué tamaño?
barco = posicionar_barco(tablero, eslora)

coloca_barcos(tablero[barco])
print(tablero)

#####################################################################

# Para articularlo supongo que habrá primero que definir las clases (tablero y barcos) y variables (barcos)
# Que luego habrá que poner las vidas (igual a las suma de las esloras) y arrancar con un bucle while de "while vidas > 0:"