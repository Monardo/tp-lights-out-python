
def mostrarNivel(nivel):
    print("    ", "A", "B", "C", "D", "E")
    ["1 | "]
    ["2 | "]
    ["3 | "]
    ["4 | "]
    ["5 | "]
    numeroDeFila = 1
    for elemento in nivel:
        linea = ''
        for subelemento in elemento:
            linea = linea +' '+ subelemento

        print (str(numeroDeFila) + "| " + (linea))
        numeroDeFila += 1