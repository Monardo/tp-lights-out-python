import unittest
import calculaSituacionJuego


class calculaSituacionJuegoTestCase(unittest.TestCase):

    def test_devuelveTrueSiTableroApagado(self):

        tablero = [["o",".","."],["o",".","."],["o",".","."]]

        calculaSituacionJuego.estaTableroCompletamenteApagado(tablero)
        return self
