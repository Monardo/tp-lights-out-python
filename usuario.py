cantidadJugadas = 0
puntaje = 0
nivelJugador = 1
nivelTablero = 1

import juego
def incrementarCantidadJuagadas():
    global cantidadJugadas
    cantidadJugadas += 1


def pasarDeNivel():
    global nivelJugador
    nivelJugador = nivelJugador + 1


