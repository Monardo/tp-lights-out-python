# Este va a ser el modo predeterminado
import nivel
import tablero
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
        tablero.mostrarNivel(nivelInicio)

        print("-------------------------------------------------")

        ingresoCoordenada = raw_input("Ingrese la coordenada :  ")
        ingresoCoordenada.lower()

        pidoCoordenada.recibeCoordenadaDeJuego(ingresoCoordenada)

        intentos += 1

