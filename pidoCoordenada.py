import tablero
import modificoTablero
import calculaSituacionJuego
import modoPredeterminado
def recibeCoordenadaDeJuego(ingresoCoordenada):
    listaLetraPermitidas = ['a', 'b', 'c', 'd', 'e']
    listaNumerosPermitidos = ['1', '2', '3', '4', '5']

    if ingresoCoordenada == 'r':
        print ("Ud ha seleccionado reiniciar el juego")
        modoPredeterminado.iniciarModoPredeterminado()

    if len(ingresoCoordenada) == 2:
        coordenasEnLetrasAPosiciones = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
        coordenadaNumerica = int(ingresoCoordenada[1])
        coordenadaLetraTransformada = coordenasEnLetrasAPosiciones[ingresoCoordenada[0]]
        coordenadaLetraTransformada = coordenadaLetraTransformada
        coordenadaEnTupla = (coordenadaLetraTransformada, coordenadaNumerica)

        if ingresoCoordenada[0] not in listaLetraPermitidas or ingresoCoordenada[1] not in listaNumerosPermitidos:
            print ("Ud ha ingresado una coordenada invalida. ")
            recibeCoordenadaDeJuego()
        else:
            nivelactual = 1
            tableroNuevo = modificoTablero.coordenadaCambiaMatriz(nivelactual, coordenadaEnTupla)
    else:
        print ("Ud ha ingresado una coordenada invalida. ")
        recibeCoordenadaDeJuego()
    jugadas = 0
    tablero.mostrarNivel(tableroNuevo)
    preguntoSiGana = calculaSituacionJuego.siTableroApagadoDevuelveTrue(tableroNuevo)
    if preguntoSiGana == True:
        print ("Ud ha ganado el juego. Felicitaciones ")
    else:
        print ("Ud lleva " + str(jugadas) + " jugadas de 15")
        jugadas += 1
    return tableroNuevo