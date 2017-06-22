import nivel
import modificoTablero
import calculaSituacionJuego
import modoPredeterminado
import usuario
import logger
import menu

def recibeCoordenadaDeJuego(ingresoCoordenada):

    listaLetraPermitidas = ['a', 'b', 'c', 'd', 'e']
    listaNumerosPermitidos = ['1', '2', '3', '4', '5']

    if ingresoCoordenada == 's':
        print("        Ud esta saliendo del juego !!!!!!!!")
        exit
        menu.saludoBienvenida()

    if ingresoCoordenada == 'r':
        print("Ud ha seleccionado reiniciar el juego")
        modoPredeterminado.iniciarModoPredeterminado()

    if ingresoCoordenada[0] not in listaLetraPermitidas or ingresoCoordenada[1] not in listaNumerosPermitidos:
        print("Ud ha ingresado una coordenada invalida ")
        ingresoCoordenada = input("Reingrese la coordenada: ")
        recibeCoordenadaDeJuego(ingresoCoordenada)

    if len(ingresoCoordenada) == 2:
        coordenasEnLetrasAPosiciones = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
        coordenadaNumerica = int(ingresoCoordenada[1])-1
        coordenadaLetraTransformada = coordenasEnLetrasAPosiciones[ingresoCoordenada[0]]
        coordenadaEnTupla = (coordenadaNumerica, coordenadaLetraTransformada)

        if coordenadaEnTupla[0] < 0 or coordenadaEnTupla[0] > 4 or coordenadaEnTupla[1] < 0 or coordenadaEnTupla[1] > 4:
            print("Ud ha ingresado una coordenada invalida. ")
            ingresoCoordenada = input("Reingrese la coordenada: ")
            recibeCoordenadaDeJuego(ingresoCoordenada)
        else:
            nivelactual = nivel.getNivel(1)
            tableroNuevo = modificoTablero.coordenadaCambiaMatriz(nivelactual, coordenadaEnTupla)

    else:
        print("Ud ha ingresado una coordenada invalida. ")
        logger.guardar("Ingreso de coordenada invalida: " + ingresoCoordenada)
        ingresoCoordenada = input("Reingrese la coordenada: ")
        recibeCoordenadaDeJuego(ingresoCoordenada)


    nivelGanado = calculaSituacionJuego.estaTableroCompletamenteApagado(tableroNuevo)

    if not nivelGanado:
        print(usuario.datosDelUsuario())

    else:
        print("Ud ha ganado el nivel. Felicitaciones.  ")

