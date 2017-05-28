import nivel
import modoPredeterminado
def coordenadaCambiaMatriz(x, y, z):
    nivelactual = x
    a = nivel.getNivel(nivelactual)
    coordenadaLetraTransformada = y
    coordenadaNumerica = z


    if a[y][z] == "o":
        a[y][z] = "."

    else:
        a[y][z] = "o"

    return a

