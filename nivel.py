
niveles = []

def getNivel(nivelactual):
    int(nivelactual)
    nivelactual = nivelactual - 1
    return niveles[nivelactual]


def cargarNivelesDesdeElArchivo():

    archivo = open("seteoDeTableros.txt", "r")

    nivel=[]

    for linea in archivo:

        lineaComoLista = linea.split()

        if ( len(lineaComoLista) > 0 ):

            if (lineaComoLista[0] != 'A'):
                nivel.append(lineaComoLista[1:])
        else:
            niveles.append(nivel)
            nivel = []

