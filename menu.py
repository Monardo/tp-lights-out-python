# Este va a ser el menu
import modoPredeterminado

def saludoBienvenida():
    print("")
    print("")
    print("                          *************************************************************************")
    print("                          ***************  BIENVENIDO AL JUEGO LIGHTS OUT !!!!!!!  ****************")
    print("                          *************************************************************************")
    print("")
    print("")

    modo = raw_input("Ingrese A para jugar en modo Aleatoreo, ingrese P para jugar en modo Predeterminado o S para salir del juego  ")
    if modo == 'S' or modo == 's':
        print("        Ud esta saliendo del juego !!!!!!!!")
        exit
    elif modo == 'A' or modo == 'a':
        print("Ud. selecciono el modo Aleatoreo")
    elif modo == 'P' or modo == 'p':
        print("Ud selecciono el modo Predeterminado")
        modoPredeterminado.iniciarModoPredeterminado()
    else:
        print("Ud ingreso un valor incorrecto, por favor ingrese nuevamente su eleccion")
        saludoBienvenida()

