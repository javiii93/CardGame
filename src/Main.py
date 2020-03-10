# --- MENU ENTREGA FASE 1 ---

import xml.etree.ElementTree as ALL
from src import LecturaXML
from src.CrearMazosOfDefEqu import arrOfCards, arrDefCards, arrEqCards
from src.MazoAleatorio import arrRandomCards
from src.Player import Player


#  Lectura de los XML
from src.PruebaLucharJugadorvsJugador import ejecutarPartida

tree = ALL.parse('xml_dtd/myBaraja.xml')
rootPlayer = tree.getroot()
tree2 = ALL.parse('xml_dtd/Enemigo.xml')
rootEnemy = tree2.getroot()

# declaracion del player y el enemy para hacer pruebas
playerPrueba=Player('Luisito Comunica')
enemyPrueba=Player('Sergio Pujol')

# Funcion para leer XML del jugador local
def case_1():
    try:
        print("\nCARGAR CARTAS PLAYER")
        print("*********************************\n")
        LecturaXML.treeLoad(rootPlayer)
    except NameError:
        print("Can't load tree")

# Funcion para leer XML del jugador enemigo
def case_2():
    try:
        print("\nCARGAR CARTAS ENEMIGO/n")
        print("*********************************\n")
        LecturaXML.treeLoad(rootEnemy)
    except NameError:
        print("Can't load tree")

# Funcion crear mazo aleatorio del jugador local
def case_3():
    print("\nCREAR MAZO ALEATORIO PLAYER/n")
    print("*********************************\n")
    playerPrueba.arrCards=arrRandomCards(rootPlayer)
    for h in range(len(playerPrueba.arrCards)):
        print(playerPrueba.arrCards[h])


# Funcion crear mazo ofensivo del jugador local
def case_4():
    print("\nCREAR MAZO OFENSIVO PLAYER/n")
    print("*********************************\n")
    playerPrueba.arrCards = arrOfCards(rootPlayer)
    for h in range(len(playerPrueba.arrCards)):
        print(playerPrueba.arrCards[h])

# Funcion crear mazo defensivo del jugador local
def case_5():
    print("\nCREAR MAZO DEFENSIVO PLAYER/n")
    print("*********************************\n")
    playerPrueba.arrCards = arrDefCards(rootPlayer)
    for h in range(len(playerPrueba.arrCards)):
        print(playerPrueba.arrCards[h])

# Funcion crear mazo equilibrado del jugador local
def case_6():
    print("\nCREAR MAZO EQUILIBRADO PLAYER/n")
    print("*********************************\n")
    playerPrueba.arrCards = arrEqCards(rootPlayer)
    for h in range(len(playerPrueba.arrCards)):
        print(playerPrueba.arrCards[h])

# Funcion crear mazo aleatorio del jugador enemigo
def case_7():
    print("\nCREAR MAZO ALEATORIO ENEMY/n")
    print("*********************************\n")
    enemyPrueba.arrCards = arrRandomCards(rootEnemy)
    for h in range(len(enemyPrueba.arrCards)):
        print(enemyPrueba.arrCards[h])

# Funcion crear mazo ofensivo del jugador enemigo
def case_8():
    print("\nCREAR MAZO OFENSIVO ENEMY/n")
    print("*********************************\n")
    enemyPrueba.arrCards = arrOfCards(rootEnemy)
    for h in range(len(enemyPrueba.arrCards)):
        print(enemyPrueba.arrCards[h])

# Funcion crear mazo defensivo del jugador enemigo
def case_9():
    print("\nCREAR MAZO DEFENSIVO ENEMY/n")
    print("*********************************\n")
    enemyPrueba.arrCards = arrDefCards(rootEnemy)
    for h in range(len(enemyPrueba.arrCards)):
        print(enemyPrueba.arrCards[h])

# Funcion crear mazo equilibrado del jugador enemigo
def case_10():
    print("\nCREAR MAZO EQUILIBRADO ENEMY/n")
    print("*********************************\n")
    enemyPrueba.arrCards = arrEqCards(rootEnemy)

    for h in range(len(enemyPrueba.arrCards)):
        print(enemyPrueba.arrCards[h])


def case_11():
    print("Luchar jugador vs jugador")
    ejecutarPartida(playerPrueba, enemyPrueba)

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
    print("11. Luchar Jugador vs Jugador")
    print("12. Luchar Jugador vs Bot (arcade)")
    print("13. Luchar Jugador vs Bot (liga)")
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

opt = 0

# repetimos el menu principal hasta que el usuario introdusca una opcion valida
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
                # Opt create enemy deck
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
            if not playerPrueba.arrCards and not enemyPrueba.arrCards:
                print("No se puede ejecutar esta opcion hasta que se hayan cargado mazos para cada jugador.")
            else:
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
