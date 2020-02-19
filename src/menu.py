import sys  # this allows you to use the sys.exit command to quit/logout of the application
import os  # This allows you to call files
import xml.etree.ElementTree as ALL

from src import LecturaXML

tree = ALL.parse('xml_dtd/myBaraja.xml')
rootPlayer = tree.getroot()
tree2 = ALL.parse('xml_dtd/Enemigo.xml')
rootEnemy = tree2.getroot()


# Funciones
# Function to clear screen in unix/lin/mac/bsd and win platforms
def borrarPantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def case_1():
    LecturaXML.treeLoad(rootEnemy)
    borrarPantalla()


def case_2():
    print("Cargar cartas enemigo")
    borrarPantalla()


def case_3():
    print("Crear mazo aleatorio")
    borrarPantalla()


def case_4():
    print("Crear mazo ofensivo")
    borrarPantalla()


def case_5():
    print("Crear mazo defensivo")
    borrarPantalla()


def case_6():
    print("Crear mazo equilibrado")
    borrarPantalla()


def case_7():
    print("Crear mazo aleatorio Enemigo")
    borrarPantalla()


def case_8():
    print("Crear mazo ofensivo Enemigo")
    borrarPantalla()


def case_9():
    print("Crear mazo defensivo Enemigo")
    borrarPantalla()


def case_10():
    print("Crear mazo equilibrado Enemigo")
    borrarPantalla()


def case_11():
    print("Luchar jugador vs jugador")
    borrarPantalla()


def case_12():
    print("Luchar jugador vs Bot(Arcade)")
    borrarPantalla()


def case_13():
    print("Luchar jugador vs Bot (Lliga)")
    borrarPantalla()


def case_14():
    print("Bye Bye")
    borrarPantalla()


def default():
    # case_14()
    print("Incorrect option. Try again!")
    borrarPantalla()


def menu():
    print("MENU PRINCIPAL")
    print("1. Cargar cartas")
    print("2. Carga cartas Enemigo")
    print("3. Crear mazo aleatorio")
    print("4. Crear mazo ofensivo")
    print("5. Crear mazo defensivo")
    print("6. Crear mazo equilibrado")
    print("7. Crear mazo aleatorio Enemigo")
    print("8. Crear mazo ofensivo Enemigo")
    print("9. Crear mazo defensivo Enemigo")
    print("10. Crear mazo equilibrado Enemigo")
    print("11. Luchar Jugador vs Jugador")
    print("12. Luchar Jugador vs Bot (arcade)")
    print("13. Luchar Jugador vs Bot (liga)")
    print("14. Salir")


# Call to functions
menu()
opt = int(input("Introduzca su opción: "))
if opt == 1:
    case_1()
elif opt == 2:
    case_2()
elif opt == 3:
    case_3()
elif opt == 4:
    case_4()
elif opt == 5:
    case_5()
elif opt == 6:
    case_6()
elif opt == 7:
    case_7()
elif opt == 8:
    case_8()
elif opt == 9:
    case_9()
elif opt == 10:
    case_10()
elif opt == 11:
    case_11()
elif opt == 12:
    case_12()
elif opt == 13:
    case_13()
elif opt == 14:
    case_14()
else:
    default()
