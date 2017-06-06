import unittest
import coordenadasVecinas


class CoordenadasVecinasTestCase(unittest.TestCase):

    def test_devuelveCoordenadasVecinasDevuelve4vecinosParaUnCentroDelTablero(self):

        tablero = [["o",".","."],["o",".","."],["o",".","."]]
        coordenadaCentral = (1,1)

        vecinos = coordenadasVecinas.devuelveCoordenadasVecinas(tablero,coordenadaCentral)
        self.assertEqual(len(vecinos),4)


    def test_devuelveCoordenadasVecinasDevuelve3vecinosParaUnCentroSuperiorDelTablero(self):
        tablero = [["o", ".", "."], ["o", ".", "."], ["o", ".", "."]]
        coordenadaCentral = (0, 1)
        vecinos = coordenadasVecinas.devuelveCoordenadasVecinas(tablero, coordenadaCentral)
        self.assertEqual(len(vecinos), 3)


    def test_devuelveCoordenadasVecinasDevuelve2vecinosParaUnVerticeDelTablero(self):
        tablero = [["o", ".", "."], ["o", ".", "."], ["o", ".", "."]]
        coordenadaCentral = (2, 2)
        vecinos = coordenadasVecinas.devuelveCoordenadasVecinas(tablero, coordenadaCentral)
        self.assertEqual(len(vecinos), 2)


