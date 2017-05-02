
def getNivelUno():
    level1=[
        ["    ", "A", "B", "C", "D", "E"],
        ["1 | ", "o", "o", ".", "o", "o"],
        ["2 | ", "o", ".", "o", ".", "o"],
        ["3 | ", ".", "o", "o", "o", "."],
        ["4 | ", "o", ".", "o", ".", "o"],
        ["5 | ", "o", "o", ".", "o", "o"],
        ]
    return level1

def mostrarNivel(nivel):
    for elemento in nivel:
        linea = ''
        for subelemento in elemento:
            linea = linea +' '+ subelemento
        print(linea)


