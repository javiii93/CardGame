import xml.etree.ElementTree as ALL
from src import LecturaXML

tree = ALL.parse('xml_dtd/myBaraja.xml')
rootPlayer = tree.getroot()
tree2 = ALL.parse('xml_dtd/Enemigo.xml')
rootEnemy = tree2.getroot()


# Functions

def case_1():
    try:
        print("\nCARGAR CARTAS PLAYER")
        print("*********************************\n")
        LecturaXML.treeLoad(rootPlayer)
    except NameError:
        print("Can't load tree")


def case_2():
    try:
        print("\nCARGAR CARTAS ENEMIGO/n")
        print("*********************************\n")
        LecturaXML.treeLoad(rootEnemy)
    except NameError:
        print("Can't load tree")


def case_3():
    print("Mazo creado.")


def case_4():
    print("Mazo creado.")


def case_5():
    print("Mazo creado.")


def case_6():
    print("Mazo creado.")


def case_7():
    print("Mazo creado.")


def case_8():
    print("Mazo creado.")


def case_9():
    print("Mazo creado.")


def case_10():
    print("Mazo creado.")


def case_11():
    print("Luchar jugador vs jugador")


def case_12():
    print("Luchar jugador vs Bot(Arcade)")


def case_13():
    print("Luchar jugador vs Bot (Lliga)")


def case_14():
    print("Bye Bye")


def default():
    print("Incorrect option. Try again!")


def menu_principal():
    print("\nMENU PRINCIPAL")
    print("*********************************\n")
    print("1. Cargar cartas")
    print("2. Carga cartas Enemigo")
    print("14. Salir")


def menu_crear_mazo():
    print("\nMENU CREAR MAZO")
    print("*********************************\n")
    print("3. Crear mazo aleatorio")
    print("4. Crear mazo ofensivo")
    print("5. Crear mazo defensivo")
    print("6. Crear mazo equilibrado")


def menu_crear_mazo_enemigo():
    print("\nMENU CREAR MAZO ENEMIGO")
    print("*********************************\n")
    print("7. Crear mazo aleatorio Enemigo")
    print("8. Crear mazo ofensivo Enemigo")
    print("9. Crear mazo defensivo Enemigo")
    print("10. Crear mazo equilibrado Enemigo")


def menu_combate():
    print("\nMENU COMBATE")
    print("*********************************\n")
    print("11. Luchar Jugador vs Jugador")
    print("12. Luchar Jugador vs Bot (arcade)")
    print("13. Luchar Jugador vs Bot (liga)")


opt = 0

while opt != 14:

    menu_principal()
    try:
        print("*********************************")
        opt = int(input("Introduzca su opción: "))

        if opt == 1:
            case_1()
            # Menu create player deck
            while opt < 3 or opt > 6:
                menu_crear_mazo()
                print("*********************************")
                opt = int(input("Introduzca su opción: "))

            # Opt create player deck
            if opt == 3:
                case_3()
            elif opt == 4:
                case_4()
            elif opt == 5:
                case_5()
            elif opt == 6:
                case_6()

        elif opt == 2:
            case_2()
            # Menu enemy deck
            while opt < 7 or opt > 11:
                menu_crear_mazo_enemigo()
                print("*********************************")
                opt = int(input("Introduzca su opción: "))
                # Opt crear mazos enemigos
                if opt == 7:
                    case_7()
                elif opt == 8:
                    case_8()
                elif opt == 9:
                    case_9()
                elif opt == 10:
                    case_10()

        # Opt to fight
        elif opt == 11:
            case_11()
        elif opt == 12:
            case_12()
        elif opt == 13:
            case_13()
        # Opt to exit and default
        elif opt == 14:
            case_14()
        else:
            default()
    except NameError:
        print("Error. Introduce un número!")
