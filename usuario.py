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

def reseteoJugadas():
    global cantidadJugadas
    cantidadJugadas = 0
    return cantidadJugadas

def incrementaPuntaje():
    global puntaje
    puntaje += 300


