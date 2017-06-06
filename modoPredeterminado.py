# Este va a ser el modo predeterminado
import nivel
import Tablero
import pidoCoordenada
import calculaSituacionJuego

def iniciarModoPredeterminado():
    intentos = 0
    while intentos < 15:

        print("")
        print("")
        print("     *********************   BIENVENIDO AL MODO PREDETERMINADO   ********************")
        print("")
        print("")
        nivelInicio = nivel.getNivel(1)
        Tablero.mostrarNivel(nivelInicio)

        print("-------------------------------------------------")

        ingresoCoordenada = input("Ingrese la coordenada :  ")
        ingresoCoordenada.lower()

        tableroNuevo = pidoCoordenada.recibeCoordenadaDeJuego(ingresoCoordenada)

        intentos += 1

