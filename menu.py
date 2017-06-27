# Este va a ser el menu
import modoPredeterminado
import logger
import juego

def saludoBienvenida():
    print("")
    print("")
    print("                          *************************************************************************")
    print("                          ***************  BIENVENIDO AL JUEGO LIGHTS OUT !!!!!!!  ****************")
    print("                          *************************************************************************")
    print("")
    print("")

    modo = input("Ingrese A para jugar en modo Aleatoreo, ingrese P para jugar en modo Predeterminado o S para salir del juego  ")
    modo.lower()
    if modo == 's':
        print("        Ud esta saliendo del juego !!!!!!!!")
        logger.cerrarArchivoLog()
        exit
    elif modo == 'a':
        print("Ud. selecciono el modo Aleatoreo")
    elif modo == 'p':
        print("Ud selecciono el modo Predeterminado")
        modoPredeterminado.iniciarModoPredeterminado()
        juego.jugar()
    else:
        print("Ud ingreso un valor incorrecto, por favor ingrese nuevamente su eleccion")
        logger.guardar("Ingreso de modo incorrecto en Menu: " + modo)
        saludoBienvenida()

