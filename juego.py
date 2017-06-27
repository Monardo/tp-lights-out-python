import nivel
import usuario
import Tablero
import pidoCoordenada
import modificoTablero
import calculaSituacionJuego
import modoPredeterminado

def jugar():
    nivelInicio = nivel.getNivel(usuario.nivelTablero)
    Tablero.mostrarNivel(nivelInicio)

    ingresoCoordenada = input("Ingrese la coordenada :  ")
    ingresoCoordenada.lower()

    pidoCoordenada.recibeCoordenadaDeJuego(ingresoCoordenada)
    nivelactual = nivel.getNivel(usuario.nivelTablero)
    coordenada = pidoCoordenada.recibeCoordenadaDeJuego(ingresoCoordenada)
    tableroNuevo = modificoTablero.coordenadaCambiaMatriz(nivelactual, coordenada)
    Tablero.mostrarNivel(tableroNuevo)
    usuario.incrementarCantidadJuagadas()
    print("Ud lleva " + str(usuario.cantidadJugadas) + " jugadas de las 15 permitidas")
    nivelGanado = calculaSituacionJuego.estaTableroCompletamenteApagado(tableroNuevo)

    if not nivelGanado:
       elniveldeljugador = usuario.nivelJugador
       print(str(elniveldeljugador))
    else:
        print("Ud ha ganado el nivel. Felicitaciones.  ")
        print("Ud tiene 300 puntos")
        queQuiereHacerElJugador = input("ingrese S para salir del juego, ingrese R para reiniciar o ingrese Y para seguir jugando ")

        if queQuiereHacerElJugador == 'Y':
            nivelactual = usuario.nivelTablero + 1
            proximoNivel = nivel.getNivel(nivelactual)
            Tablero.mostrarNivel(proximoNivel)

        if queQuiereHacerElJugador == 'S':
            print("        Ud esta saliendo del juego !!!!!!!!")
            exit
            menu.saludoBienvenida()

        if queQuiereHacerElJugador == 'R':
            print("Ud ha seleccionado reiniciar el juego")
            modoPredeterminado.iniciarModoPredeterminado()
