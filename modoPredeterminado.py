# Este va a ser el modo predeterminado
import nivel
import tablero
def iniciarModoPredeterminado():
    nivelactual = 1
    print("")
    print("")
    print("     *********************   BIENVENIDO AL MODO PREDETERMINADO   ********************")
    print("")
    print("")
    nivelactual = nivel.getNivel(1)
    tablero.mostrarNivel(nivelactual)

    print("-------------------------------------------------")

    listaLetraPermitidas = ['a', 'b', 'c', 'd', 'e']
    listaNumerosPermitidos = ['1', '2', '3', '4', '5']
    ingresoCoordenada = raw_input("Ingrese la coordenada :  ")
    ingresoCoordenada.lower()

    if ingresoCoordenada == 'r':
        print ("Ud ha seleccionado reiniciar el juego")
        iniciarModoPredeterminado()

    if len(ingresoCoordenada) == 2:
        if ingresoCoordenada[0] not in listaLetraPermitidas or ingresoCoordenada[1] not in listaNumerosPermitidos:
            print ("Ud ha ingresado una coordenada invalida. ")
            iniciarModoPredeterminado()
    else:
        print ("Ud ha ingresado una coordenada invalida. ")
        iniciarModoPredeterminado()

    coordenasEnLetrasAPosiciones = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}


    coordenadaNumerica = int(ingresoCoordenada[1])

    coordenadaLetraTransformada = coordenasEnLetrasAPosiciones[ingresoCoordenada[0]]

    coordenadaLetraTransformada = coordenadaLetraTransformada
    print coordenadaLetraTransformada
    print coordenadaNumerica - 1

