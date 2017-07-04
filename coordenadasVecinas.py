def eliminaVecinosInvalidos(vecinos, tamaño):

    vecinosValidos = []

    for tupla in vecinos:
        if tupla[0] >= 0 and tupla[1] >= 0 and tupla[0] < tamaño and tupla[1] < tamaño:

            vecinosValidos.append(tupla)

    return vecinosValidos


def devuelveCoordenadasVecinas(tablero, coordenadaEnTupla):

    tamaño = len(tablero)
    fila = coordenadaEnTupla[0]
    columna = coordenadaEnTupla[1]

    coordenadaVecinoSuperior = (fila-1,columna)
    coordenadaVecinoInferior = (fila+1, columna)
    coordenadaVecinoIzquierda = (fila, columna-1)
    coordenadaVecinoDerecha = (fila, columna+1)

    vecinos = [coordenadaVecinoSuperior, coordenadaVecinoInferior, coordenadaVecinoIzquierda, coordenadaVecinoDerecha]

    return eliminaVecinosInvalidos(vecinos, tamaño)

