# --- MENU ENTREGA FASE 3 ---

import xml.etree.ElementTree as ALL
from src import LecturaXML
from src.CrearMazosOfDefEqu import arrOfCards, arrDefCards, arrEqCards
from src.MazoAleatorio import arrRandomCards
from src.Player import Player


#  Lectura de los XML
from src.Luchar_jugador_vs_jugador import ejecutarPartida
from src.Luchar_jugador_vs_jugador_liga import ligaSantander


tree = ALL.parse('xml_dtd/myBaraja.xml')
rootPlayer = tree.getroot()
tree2 = ALL.parse('xml_dtd/Enemigo.xml')
rootEnemy = tree2.getroot()

# declaracion del player y el enemy
localPlayer=Player('local')
enemyPlayer=Player('enemigo')

# Declaracion del clone del jugador local y asigncion de un mazo aleatorio
playerClone=Player('Computadora')
playerClone.arrCards=arrRandomCards(rootPlayer)


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
    localPlayer.arrCards=arrRandomCards(rootPlayer)
    for h in range(len(localPlayer.arrCards)):
        print(localPlayer.arrCards[h])


# Funcion crear mazo ofensivo del jugador local
def case_4():
    print("\nCREAR MAZO OFENSIVO PLAYER/n")
    print("*********************************\n")
    localPlayer.arrCards = arrOfCards(rootPlayer)
    for h in range(len(localPlayer.arrCards)):
        print(localPlayer.arrCards[h])

# Funcion crear mazo defensivo del jugador local
def case_5():
    print("\nCREAR MAZO DEFENSIVO PLAYER/n")
    print("*********************************\n")
    localPlayer.arrCards = arrDefCards(rootPlayer)
    for h in range(len(localPlayer.arrCards)):
        print(localPlayer.arrCards[h])

# Funcion crear mazo equilibrado del jugador local
def case_6():
    print("\nCREAR MAZO EQUILIBRADO PLAYER/n")
    print("*********************************\n")
    localPlayer.arrCards = arrEqCards(rootPlayer)
    for h in range(len(localPlayer.arrCards)):
        print(localPlayer.arrCards[h])

# Funcion crear mazo aleatorio del jugador enemigo
def case_7():
    print("\nCREAR MAZO ALEATORIO ENEMY/n")
    print("*********************************\n")
    enemyPlayer.arrCards = arrRandomCards(rootEnemy)
    for h in range(len(enemyPlayer.arrCards)):
        print(enemyPlayer.arrCards[h])

# Funcion crear mazo ofensivo del jugador enemigo
def case_8():
    print("\nCREAR MAZO OFENSIVO ENEMY/n")
    print("*********************************\n")
    enemyPlayer.arrCards = arrOfCards(rootEnemy)
    for h in range(len(enemyPlayer.arrCards)):
        print(enemyPlayer.arrCards[h])

# Funcion crear mazo defensivo del jugador enemigo
def case_9():
    print("\nCREAR MAZO DEFENSIVO ENEMY/n")
    print("*********************************\n")
    enemyPlayer.arrCards = arrDefCards(rootEnemy)
    for h in range(len(enemyPlayer.arrCards)):
        print(enemyPlayer.arrCards[h])

# Funcion crear mazo equilibrado del jugador enemigo
def case_10():
    print("\nCREAR MAZO EQUILIBRADO ENEMY/n")
    print("*********************************\n")
    enemyPlayer.arrCards = arrEqCards(rootEnemy)

    for h in range(len(enemyPlayer.arrCards)):
        print(enemyPlayer.arrCards[h])


def case_11():
    print("Luchar jugador vs jugador")
    ejecutarPartida(localPlayer, enemyPlayer)

def case_12():
    print("Luchar jugador vs Bot(Arcade)")
    ejecutarPartida(localPlayer, playerClone)

def case_13():
    arrPlayer = []
    randomPlayer1 = Player('1')
    randomPlayer2 = Player('2')
    randomPlayer3 = Player('3')
    randomPlayer4 = Player('4')
    randomPlayer5 = Player('5')
    randomPlayer6 = Player('6')
    randomPlayer1.arrCards = arrRandomCards(rootPlayer)
    randomPlayer2.arrCards = arrRandomCards(rootPlayer)
    randomPlayer3.arrCards = arrRandomCards(rootPlayer)
    randomPlayer4.arrCards = arrRandomCards(rootPlayer)
    randomPlayer5.arrCards = arrRandomCards(rootPlayer)
    randomPlayer6.arrCards = arrRandomCards(rootPlayer)
    arrPlayer.append(randomPlayer1)
    arrPlayer.append(randomPlayer2)
    arrPlayer.append(randomPlayer3)
    arrPlayer.append(randomPlayer4)
    arrPlayer.append(randomPlayer5)
    arrPlayer.append(randomPlayer6)
    print("Luchar jugador vs Bot (Lliga, 6 jugadores)")
    contador = 0;
    jornada = 1;
    ligaSantander(arrPlayer, contador, jornada)


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
            if not localPlayer.arrCards or not enemyPlayer.arrCards:
                print("No se puede ejecutar esta opcion hasta que se hayan cargado mazos para cada jugador.")
            else:
                case_11()
        elif opt == 12:
            if not localPlayer.arrCards:
                print("No se puede ejecutar esta opcion hasta que se hayan cargado mazos para cada jugador.")
            else:
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
