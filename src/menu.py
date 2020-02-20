# --- MENU ENTREGA FASE 1 ---

import sys  # this allows you to use the sys.exit command to quit/logout of the application
import os  # This allows you to call files
import xml.etree.ElementTree as ALL

from src import LecturaXML

#Lectura de los XML
tree = ALL.parse('xml_dtd/myBaraja.xml')
rootPlayer = tree.getroot()
tree2 = ALL.parse('xml_dtd/Enemigo.xml')
rootEnemy = tree2.getroot()


# Funciones

#Funcion para leer XML del jugador local
def case_1():
   try:
       LecturaXML.treeLoad(rootPlayer)
   except:
       print("Can't load tree")

#Funcion para leer XML del jugador enemigo
def case_2():
   try:
       LecturaXML.treeLoad(rootEnemy)
   except:
       print("Can't load tree")

#Funcion crear mazo aleatorio del jugador local
def case_3():
   print("Mazo creado.")

#Funcion crear mazo ofensivo del jugador local
def case_4():
   print("Mazo creado.")

#Funcion crear mazo defensivo del jugador local
def case_5():
   print("Mazo creado.")

#Funcion crear mazo equilibrado del jugador local
def case_6():
   print("Mazo creado.")

#Funcion crear mazo aleatorio del enemigo
def case_7():
   print("Mazo creado.")

#Funcion crear mazo ofensivo del enemigo
def case_8():
   print("Mazo creado.")

#Funcion crear mazo defensivo del enemigo
def case_9():
   print("Mazo creado.")

#Funcion crear mazo equilibrado del enemigo
def case_10():
   print("Mazo creado.")


def case_11():
   print("Luchar jugador vs jugador")


def case_12():
   print("Luchar jugador vs Bot(Arcade)")


def case_13():
   print("Luchar jugador vs Bot (Lliga)")

#Funcion para mostrar mensage de fin de programa
def case_14():
   print("Bye Bye")


def default():
   print("Incorrect option. Try again!")


def menu_principal():
   print("MENU PRINCIPAL")
   print("1. Cargar cartas")
   print("2. Carga cartas Enemigo")
   print("14. Salir")


def menu_crear_mazo():
   print("3. Crear mazo aleatorio")
   print("4. Crear mazo ofensivo")
   print("5. Crear mazo defensivo")
   print("6. Crear mazo equilibrado")


def menu_crear_mazo_enemigo():
   print("7. Crear mazo aleatorio Enemigo")
   print("8. Crear mazo ofensivo Enemigo")
   print("9. Crear mazo defensivo Enemigo")
   print("10. Crear mazo equilibrado Enemigo")


def menu_combate():
   print("11. Luchar Jugador vs Jugador")
   print("12. Luchar Jugador vs Bot (arcade)")
   print("13. Luchar Jugador vs Bot (liga)")


opt = 0

while opt != 14: #repetimos el menu principal hasta que el usuario introdusca una opcion valida

   menu_principal()
   try:
       opt = int(input("Introduzca su opción: "))

       if opt == 1:
           case_1()
           while opt < 3 or opt > 6: #reptimos el menu crear mazo hasta que el usuario introducas una opcion valida
               menu_crear_mazo()
               opt = int(input("Introduzca su opción: "))

           if opt == 3:
               case_3()
           elif opt == 4:
               case_4()
           elif opt == 5:
               case_5()

       elif opt == 2:
           case_2()

           while opt < 7 or opt > 11:  #reptimos el menu crear mazo enemigo hasta que el usuario introducas una opcion valida
               menu_crear_mazo_enemigo()
               opt = int(input("Introduzca su opción: "))

               if opt == 7:
                   case_7()
               elif opt == 8:
                   case_8()
               elif opt == 9:
                   case_9()
               elif opt == 10:
                   case_10()
       else:
           default()
   except:
       print("Opcion incorrecta.")
