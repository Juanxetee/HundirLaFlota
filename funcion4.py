# Notas Marce

# Lo de inicializar el tablero (que primero debe estar vacío) para poblarlo con barcos, ¿no son 2 pasos diferentes (1: crear 2: poblar)?
# por qué los barcos ya están dentro de la clase Tablero?

# En clases no hay que inicializar un tercer tablero?
tab0 = Tablero() # sería el tablero vacío que se genera al inicializar la clase tablero, no?
tab1 = Tablero(id_jugador="juancho") 
# Esos serían los barcos de jugador 1 donde primero se imprimen los barcos y se le sobreescriben los disparos de la máquina
tab2 = Tablero(id_jugador="juancho") 
# Y este otro el de los disparos de jugador 1. ¿Iría con mismo id_jugador???

# No se define en la propia clase Tablero que son 2 jugadores, por ej: id_jugador1 e id_jugador2, 
# y que al iniciar se le pregunte al jugador humano su nombre y con eso reemplace el "id_jugador1"?
# de alguna forma tenemos que poder hacer el pase de un jugador al otro y llevar el registro separado de los barcos, aciertos, vidas...
# ¿Tiene sentido crear un objeto jugador, que tenga su id (que puede ser remplazado por el alias que el usuario quiera, 
# que muestre a su vez las vidas que le quedan / su flota? 

# Y si al tablero le ponemos que el índice de los arrays sea una letra, en lugar de número, y el jugador entra una letra y un número, 
# como en el juego de toda la vida, y así la A es el índice 0, la B el 1

# En las instrucciones se recomienda crear una clase barcos. 
# No se me ocurre qué atributos pueden tener más allá de la eslora... 
# Un identificador del tablero o jugador al que pertenecen?
class Barco:
# Aquí definiríamos los atributos y métodos de la clase barcos
    def __init__(self, eslora):
        self.eslora = eslora


vidas = [0]
for barco in barcos:
    vidas += eslora(barco)

# Poner los barcos en el tablero
def coloca_barcos(tablero, barcos):
    for barco in barcos:
        for c in barco:
            tablero[c] = "\U0001F6A2" # Unicode de "ship"

barcos = [[],[]] # Esto sellena con una lista por barco, que a su vez tiene las tuplas de las coordenadas de cada casillero
# se hará una por jugador, no?
coloca_barcos(tab1, barcos) # Entiendo que le damos el parámetro del tablero del jugador
print(tab1)



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
# Esto mismo, pero adaptado, no se podría usar para verificar que las coordenadas del usuario están efectivamente dentro del tablero
# Y en caso contrario indicar que no es correcto, que lo vuelva a poner



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

# Disparar

def coord_disparo
# si es player_2, con randchoice + randint se define la coordenada
# Si es player_1 persona se le pide y comprueba que sea una letra y número en los rangos adecuados.
# de lo comtrario se le sigue pidiendo en bucle hasta que de coordenada válida


def comprobar_disparo(tablero, coordenada):
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
# # No me queda claro qué opción sería else, ya que o hay barco o hay agua... 
# a menos que sea una coordenada de fuera del tablero y haya que dar un mensaje de error, no solo pass...
# igualmente con los tableros, que si juega el jugador1, es en el tablero "oculto" que se refleja el acierto o errada, y viceversa
# Aqui se puede añadir algo de acierto = False / que cambie de usuario. 
    # tipo return acierto = False / True
# A menos que se acierte y cambie a True, en cuyo caso reinicia este bucle (o a la inversa, por defecto en loop pero si falla se corta)
    
disparar(tab1,()) # va la tupla con las coordenadas
print(tablero) 

# Hay que hacer el cambio de jugador. Y si le toca al humano, pedirle de nuevo una coordenada. si es la máquina, que dispare
# es solo la idea para desarrollar, pero mal expresada
# al inicializar el tablero debería haber un inico que determine que quien empieza es el humano, que puede ser id_jugador 1
# Y En cada jugada debería estar activado el id_usuario, en cada turno
def cambio_jugador(id_jugador):
    if acierto == False: # es decir, si el jugador que estaba jugando falla, hay cambio
        player_activo != id_player # el jugador activo ahora pasa a ser diferente al de la jugada anterior
        if player_activo # es el humano
            print("Es tu turno. Introduce las coordenadas:")
            # Y de alguna forma esto deberia definir las coordenadas de la siguiente jugada del humano, no de la máquina
        else:
            # si le toca a la máquina, que active la función de disparar con parámetros aleatorios

# Y falta cerrar el bucle while de las vidas, una vez que se quede sin vidas alguno de los dos
# es solo la idea, seguramente mal expresada
def fin_partida(id_player, vidas):
    if id_player_1[vidas] = 0:
        print("Toda tu flota seha hundido. Fin del juego")       
    elif:
        print("¡Felicidades. Has hundido toos los barcos!.")
    print(tab1)
    print(tab2)
    en_juego = False # que al inicio de la partida podría estar predefinida en True


# Y esto ya parecería ser el juego:
# con esto se define el punto de partida, la coordenada inicial más la orientación
ancho, largo, o = barco_aleatorio(len(tablero))
print(f"Tentativa de barco. Posición inicial: [{ancho}][{largo}], y orientación: {o}")

# En este siguiente paso se generan las coordenadas, una para cada casillero (eslora) del barco
eslora = x 
# ¿Puede ser quehaya que hacer un bucle for que recorra la flota entera, cada barco con su eslora, 
# para que genere un barco aleatorio por cada elemento de la flota con su tamaño correspondiente?
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