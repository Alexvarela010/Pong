from menu import Menu


def mostrar_menu():
    menu = Menu()
    return menu.mostrar()

if __name__ == "__main__":
    while True:  # Mantener el ciclo principal
        # Mostrar el menú

        modo_juego = mostrar_menu()



