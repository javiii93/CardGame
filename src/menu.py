import sys  # this allows you to use the sys.exit command to quit/logout of the application
import os # This allows you to call files


#Funciones
def case_1():
   print ("Cargar cartas")

def case_2():
    print ("Cargar cartas enemigo")

def case_3():
    print ("Crear mazo aleatorio")

def case_4():
    print ("Crear mazo ofensivo")

def case_5():
    print ("Crear mazo defensivo")

def case_6():
    print ("Crear mazo equilibrado")

def case_7():
    print ("Crear mazo aleatorio Enemigo")

def case_8():
    print ("Crear mazo ofensivo Enemigo")

def case_9():
    print ("Crear mazo defensivo Enemigo")

def case_10():
    print ("Crear mazo equilibrado Enemigo")

def case_11():
    print ("Luchar jugador vs jugador")

def case_12():
    print ("Luchar jugador vs Bot(Arcade)")

def case_13():
    print ("Luchar jugador vs Bot (Lliga)")

def case_14():
    print ("Bye Bye")

def default():
    print ("Incorrect option")



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
opt = int(input("Introduzca su opción: "))

#Call to functions

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
if opt == 9:
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