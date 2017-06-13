
def estaTableroCompletamenteApagado(tableroNuevo):

    for fila in tableroNuevo:
        for celda in fila:
            if celda == 'o':
                return False

    return True
