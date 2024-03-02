#main.py

def generar_barco_aleatorio(self, tablero, longitud): 
        filas, columnas = tablero.shape
        fila = np.random.randint(0, filas - 1)
        columna = np.random.randint(0, columnas - 1)
        orientacion = np.random.choice(['N', 'S', 'O', 'E'])
        while not self.validar_posicion(fila, columna, orientacion): # Va a llamar a la funcion posicionar barco hasta que devuelva true, una vez sea true otorga los valores random en el lugar que dio true
            fila = np.random.randint(0, filas - 1)
            columna = np.random.randint(0, columnas - 1)
            orientacion = np.random.choice(['N', 'S', 'O', 'E'])