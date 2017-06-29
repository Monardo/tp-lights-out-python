nivel1 = []
nivel2 = []
nivel3 = []
nivel4 = []
nivel5 = []

niveles = [nivel1,nivel2,nivel3,nivel4,nivel5]

def getNivel(nivelactual):
    int(nivelactual)
    nivelactual = nivelactual - 1
    return niveles[nivelactual]


def cargarNivelesDesdeElArchivo():
    archivo = open("seteoDeTableros.txt", "r")
    return archivo

def cargarNivel():

    archivoDeNiveles = cargarNivelesDesdeElArchivo()

    for linea in archivoDeNiveles:
        linea = linea.rstrip("\n")
        nivel1.append(linea)
        if linea == "":
            break


    print(nivel1)


    print(linea)

cargarNivel()
