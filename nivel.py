# se desarrollara el nivel 1 del juego

def getNivelUno():
    level1_0=["  ", "A", "B", "C", "D", "E"]
    level1_1=["1/", "o", "o", ".", "o", "o"]
    level1_2=["2/", "o", ".", "o", ".", "o"]
    level1_3=["3/", ".", "o", "o", "o", "."]
    level1_4=["4/", "o", ".", "o", ".", "o"]
    level1_5=["5/", "o", "o", ".", "o", "o"]

    return  [level1_0, level1_1, level1_2, level1_3, level1_4, level1_5]

def mostrarNivel(nivel):
    print(nivel)


def recorrerArray():
    for i in range(0, 5):
        print(getNivelUno())
recorrerArray()

