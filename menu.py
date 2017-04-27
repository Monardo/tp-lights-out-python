# Este va a ser el menu
import modoPredeterminado

def saludoBienvenida():
    print()
    print()
    print("                          *************************************************************************")
    print("                          ***************  BIENVENIDO AL JUEGO LIGHTS OUT !!!!!!!  ****************")
    print("                          *************************************************************************")
    print()
    print()

    modo=input(print("Ingrese A para jugar en modo Aleatoreo, ingrese P para jugar en modo Predeterminado o S para salir del juego"))
    if modo == 'S' or modo == 's':
        print("        Ud está saliendo del juego !!!!!!!!")
        exit
    elif modo == 'A' or modo == 'a':
        print("Ud. seleccionó el modo Aleatoreo")
    elif modo == 'P' or modo == 'p':
        print("Ud seleccionó el modo Predeterminado")
        modoPredeterminado.iniciarModoPredeterminado()
    else:
        print("Ud ingreso un valor incorrecto, por favor ingrese nuevamente su eleccion")
        saludoBienvenida()

