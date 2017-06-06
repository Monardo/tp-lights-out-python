import coordenadasVecinas

def coordenadaCambiaMatriz(tablero, coordenadaEnTupla):

    vecinas = coordenadasVecinas.devuelveCoordenadasVecinas(tablero,coordenadaEnTupla)

    if tablero[coordenadaEnTupla[0]] [coordenadaEnTupla[1]] == "o":
        tablero[coordenadaEnTupla[0]] [coordenadaEnTupla[1]] = "."
    else:
        tablero[coordenadaEnTupla[0]] [coordenadaEnTupla[1]] = "o"

    #recorrer la lista de coordernadas vecinas y por cada una cambiar su valor, tambien cambiar el valor de la coordenadas

    for elemento in vecinas:
        fila = int(elemento[0])
        columna = int(elemento[1])
        if tablero [fila][columna] == "o":
            tablero [fila][columna] = "."
        else:
            tablero[fila][columna] = "o"

    return tablero