import nivel
import usuario
import Tablero
import pidoCoordenada
import modificoTablero
import calculaSituacionJuego
import modoPredeterminado
import menu

def jugar():

    if usuario.cantidadJugadas == 0 and usuario.nivelJugador == 1:

       nivelInicio = nivel.getNivel(usuario.nivelJugador)
       Tablero.mostrarNivel(nivelInicio)



    if usuario.cantidadJugadas == 15:
        print("***********  P E R D I O  ************")
        menu.saludoBienvenida()

    nivelactual = nivel.getNivel(usuario.nivelJugador)
    print("")
    ingresoCoordenada = input("Ingrese la coordenada :  ")
    ingresoCoordenada.lower()

    coordenada = pidoCoordenada.recibeCoordenadaDeJuego(ingresoCoordenada)
    tableroNuevo = modificoTablero.coordenadaCambiaMatriz(nivelactual, coordenada)
    print("")
    Tablero.mostrarNivel(tableroNuevo)
    usuario.incrementarCantidadJuagadas()
    print("")
    print("Ud lleva " + str(usuario.cantidadJugadas) + " jugadas de 15 permitidas")
    nivelGanado = calculaSituacionJuego.estaTableroCompletamenteApagado(tableroNuevo)

    if not nivelGanado:
       elniveldeljugador = usuario.nivelJugador
       print("Nivel " + str(elniveldeljugador))
       jugar()
    else:
        print("")
        print("Ud ha ganado el nivel. Felicitaciones.  ")
        usuario.incrementaPuntaje()
        print("Ud tiene " + str(usuario.puntaje) + " puntos")
        print("")
        queQuiereHacerElJugador = str(input("ingrese S para salir del juego, ingrese R para reiniciar o ingrese Y para seguir jugando "))
        queQuiereHacerElJugador.lower()
        if queQuiereHacerElJugador == 'y':
            nivelactual = usuario.nivelTablero + 1
            proximoNivel = nivel.getNivel(nivelactual)
            usuario.pasarDeNivel()
            usuario.reseteoJugadas()
            Tablero.mostrarNivel(proximoNivel)
            jugar()

        if queQuiereHacerElJugador == 's':
            print("        Ud esta saliendo del juego !!!!!!!!")
            exit
            menu.saludoBienvenida()

        if queQuiereHacerElJugador == 'r':
            print("Ud ha seleccionado reiniciar el juego")
            modoPredeterminado.iniciarModoPredeterminado()
