# Este va a ser el menu

def saludoBienvenida():
    print("Bienvenido al juego Lights Out")
    modo=input(print("Ingrese A para jugar en modo Aleatoreo, ingrese P para jugar en modo Predeterminado o S para salir del juego"))
    if modo == 'S':
        print("Ud ha salido del juego")
    elif modo == 'A':
        print("Ud. seleccionó el modo Aleatoreo")
    elif modo == 'P':
        print("Ud seleccionó el modo Predeterminado")
    else:
        print("Ud ingreso un valor incorrecto, por favor ingrese nuevamente su eleccion")

