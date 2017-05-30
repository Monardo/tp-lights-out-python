import nivel
import modoPredeterminado
def coordenadaCambiaMatriz(nivelactual, coordenadas):

    tablero = nivel.getNivel(nivelactual)
    coordenadasVecinas = getCoordenadasVecinas(tablero,coordenadas)

    #recorrer la lista de coordernadas vecinas y por cada una cambiar su valor, tambien cambiar el valor de la coordenadas