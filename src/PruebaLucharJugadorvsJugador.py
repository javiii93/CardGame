#lista de diccionarios Python
import xml.etree.ElementTree as ALL
from random import randint
from src.MazoAleatorio import arrRandomCards
from src.Player import Player

tree = ALL.parse('xml_dtd/myBaraja.xml')
rootPlayer = tree.getroot()

arrCard1 = arrRandomCards()
arrCard2 = arrRandomCards()

jugador1 = Player('Jugador1', arrCard1)
jugador2 = Player('Jugador2', arrCard2)

def randomNumArray10():
    arr = []
    for i in range(10):
        value = randint(1, 10)
        # Hay que comprobar si el nuevo numero aleatorio esta en el array.
        while (value in arr):
            value = randint(1, 10)
        arr.append(value)
    return arr


def invocacion(jugador1): #parametros: jugador local o enemigo
    #reiniciar puntos de invocacion del jugador a 5
    jugador1.summonPoints = 5
    #Crear array de las cartas del turno
    arrCardTurnPlayer1 = []
    #seleccionar cartas aleatorias del mazo hasta agotar puntos de invocacion e ir metiendo las cartas en el array de cartas del turno
    arr = randomNumArray10()
    posicionArr = 0
    while jugador1.summonPoints < 0:
        arrCardTurnPlayer1[posicionArr] = jugador1.arrCards[arr[posicionArr]]
        if jugador1.summonPoints - jugador1.arrCards[arr[posicionArr]].summonPoints:
            jugador1.summonPoints = jugador1.summonPoints - jugador1.arrCards[arr[posicionArr]].summonPoints
        posicionArr = posicionArr + 1




def destino():
    value = randint(1,2)
    return value

def confrontacion(arg): #parametros : jugador local y jugador enemigo



