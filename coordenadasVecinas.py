
def eliminaVecinosInvalidos(vecinos):

    vecinosValidos = []

    for tupla in vecinos:

        if tupla[0] >= 0 and tupla[1] >= 0:

            vecinosValidos.append(tupla)

    return vecinosValidos


def devuelveCoordenadasVecinas(tablero, coordenadaEnTupla):
    vecinos = []

    fila = coordenadaEnTupla[0]
    columna = coordenadaEnTupla[1]

    coordenadaVecinoSuperior = (fila-1,columna)
    coordenadaVecinoInferior = (fila+1, columna)
    coordenadaVecinoIzquierda = (fila, columna-1)
    coordenadaVecinoDerecha = (fila, columna+1)

    vecinos = [coordenadaVecinoSuperior, coordenadaVecinoInferior, coordenadaVecinoIzquierda, coordenadaVecinoDerecha]

    return eliminaVecinosInvalidos(vecinos)

