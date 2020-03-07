#lista de diccionarios Python
import xml.etree.ElementTree as ALL
from random import randint

from src.Card import Card
from src.MazoAleatorio import arrRandomCards
from src.Player import Player

tree = ALL.parse('xml_dtd/myBaraja.xml')
rootPlayer = tree.getroot()

arrCard1 = arrRandomCards(rootPlayer)
arrCard2 = arrRandomCards(rootPlayer)

#for h in range(len(arrCard1)):
#    print(arrCard1[h])
#print("********")
#for h in range(len(arrCard2)):
#    print(arrCard2[h])

jugador1 = Player('Jugador1', arrCard1)
jugador2 = Player('Jugador2', arrCard2)

print("Cartas mazo jugador 1 :")
for h in range(len(jugador1.arrCards)):
    print(jugador1.arrCards[h])
print("Cartas mazo jugador 2 :")
for h in range(len(jugador2.arrCards)):
    print(jugador2.arrCards[h])

print("***** TURNO 1 *******")

def randomNumArray10():
    arr = []
    for i in range(10):
        value = randint(0, 9)
        # Hay que comprobar si el nuevo numero aleatorio esta en el array.
        while (value in arr):
            value = randint(0, 9)
        arr.append(value)
    return arr

def invocacion(jugador1): #parametros: jugador local o enemigo
    #reiniciar puntos de invocacion del jugador a 5
    jugador1.summonPoints = 5
    #Crear array de las cartas del turno
    arrCardTurnPlayer = []
    #seleccionar cartas aleatorias del mazo hasta agotar puntos de invocacion e ir metiendo las cartas en el array de cartas del turno
    randomArray = randomNumArray10()
    arrayIndex = 0
    while jugador1.summonPoints > 0 and arrayIndex < 10:
        #print("Sum Points :")
        #print(jugador1.summonPoints)
        #print("ArrayIndex :")
        #print(arrayIndex)
        #print("Numero de carta en el maz :")
        #print(randomArray[arrayIndex])
        if (jugador1.summonPoints - int(jugador1.arrCards[randomArray[arrayIndex]].summonPoints)) >= 0:
            jugador1.summonPoints = jugador1.summonPoints - int(jugador1.arrCards[randomArray[arrayIndex]].summonPoints)
            arrCardTurnPlayer.append((jugador1.arrCards[randomArray[arrayIndex]]))
        arrayIndex = arrayIndex + 1
    return arrCardTurnPlayer


arrCardTurnPlayer1 = invocacion(jugador1)
arrCardTurnPlayer2 = invocacion(jugador2)
print("cartas turno jugador 1 :")

for h in range(len(arrCardTurnPlayer1)):
    print(arrCardTurnPlayer1[h])
print("cartas turno jugador 2 :")
for h in range(len(arrCardTurnPlayer2)):
    print(arrCardTurnPlayer2[h])

def destino():
    value = randint(1,2)
    return value

def confrontacion(jugador1, jugador2): #parametros : jugador local y jugador enemigo
    valorDestino = destino()
    print("valor destino = ", valorDestino)
    continuarCiclo = 0
    if valorDestino == 1:
        while jugador1.life > 0 and jugador2.life > 0 and len(arrCardTurnPlayer1) > 0 and len(arrCardTurnPlayer2) > 0:
            danoPorCiclo = 0
            dano = 0
            print("+++++ CICLO +++++")
            print("vidas  jugador1", jugador1.life, " jugador2 ", jugador2.life)
            for indexCardTurn in range(0,len(arrCardTurnPlayer1)):
                print("----- ATAQUE ------")
                print(jugador1.name," ", arrCardTurnPlayer1[indexCardTurn])

                if indexCardTurn < len(arrCardTurnPlayer2):
                    print(jugador2.name, " ", arrCardTurnPlayer2[indexCardTurn])
                    dano = peleaCartas(indexCardTurn, arrCardTurnPlayer1, arrCardTurnPlayer2, jugador2)
                    print(dano)
                    danoPorCiclo = danoPorCiclo + dano
                else:
                    jugador2.life = int(jugador2.life) - int(arrCardTurnPlayer1[indexCardTurn].attack)
                print("vidas  jugador1", jugador1.life, " jugador2 ", jugador2.life)
            if jugador2.life > 0:
                for indexCardTurn in range(0,len(arrCardTurnPlayer2)):
                    print("----- ATAQUE ------")
                    print(jugador2.name, " ", arrCardTurnPlayer2[indexCardTurn])

                    if indexCardTurn < len(arrCardTurnPlayer1):
                        print(jugador1.name, " ", arrCardTurnPlayer1[indexCardTurn])
                        dano = peleaCartas(indexCardTurn, arrCardTurnPlayer2, arrCardTurnPlayer1, jugador1)
                        print(dano)
                        danoPorCiclo = danoPorCiclo + dano
                    else:
                        jugador1.life = int(jugador1.life) - int(arrCardTurnPlayer2[indexCardTurn].attack)
                    print("vidas  jugador1", jugador1.life, " jugador2 ", jugador2.life)
            print(danoPorCiclo)
            print("Danos recibidos por el jugador ", jugador1.name, " ", 10 - jugador1.life)
            print("Danos recibidos por el jugador ", jugador2.name, " ", 10 - jugador2.life)
            if jugador1.life <= 0:
                print("El jugador ", jugador1.name, " ha sido eliminado.")
            if jugador2.life <= 0:
                print("El jugador ", jugador2.name, " ha sido eliminado.")
            if danoPorCiclo == 0:
                print("Cerramos bucle")
                break

    if valorDestino == 2:
        while jugador1.life > 0 and jugador2.life > 0 and len(arrCardTurnPlayer1) > 0 and len(arrCardTurnPlayer2) > 0:
            danoPorCiclo = 0
            dano = 0
            print("+++++ CICLO +++++")
            print("vidas  jugador1", jugador1.life, " jugador2 ", jugador2.life)
            for indexCardTurn in range(0,len(arrCardTurnPlayer2)):
                print("----- ATAQUE ------")
                print(jugador2.name, " ", arrCardTurnPlayer2[indexCardTurn])
                if indexCardTurn < len(arrCardTurnPlayer1):
                    print(jugador1.name, " ", arrCardTurnPlayer1[indexCardTurn])
                    dano = peleaCartas(indexCardTurn, arrCardTurnPlayer2, arrCardTurnPlayer1, jugador1)
                    print(dano)
                    danoPorCiclo = danoPorCiclo + dano
                else:
                    jugador1.life = int(jugador1.life) - int(arrCardTurnPlayer2[indexCardTurn].attack)
                print("vidas  jugador1", jugador1.life, " jugador2 ", jugador2.life)
            if jugador1.life > 0:
                for indexCardTurn in range(0,len(arrCardTurnPlayer1)):
                    print("----- ATAQUE ------")
                    print(jugador1.name, " ", arrCardTurnPlayer1[indexCardTurn])
                    if indexCardTurn < len(arrCardTurnPlayer2):
                       print(jugador2.name, " ", arrCardTurnPlayer2[indexCardTurn])
                       dano = peleaCartas(indexCardTurn, arrCardTurnPlayer1, arrCardTurnPlayer2, jugador2)
                       print("LALALAL", dano)
                       danoPorCiclo = danoPorCiclo + dano
                    else:
                        jugador2.life = int(jugador2.life) - int(arrCardTurnPlayer1[indexCardTurn].attack)
                    print("vidas  jugador1", jugador1.life, " jugador2 ", jugador2.life)
            print(danoPorCiclo)
            print("Danos recibidos por el jugador ", jugador1.name, " ", 10 - jugador1.life)
            print("Danos recibidos por el jugador ", jugador2.name, " ", 10 - jugador2.life)
            if jugador1.life <= 0:
                print("El jugador ", jugador1.name, " ha sido eliminado.")
            if jugador2.life <= 0:
                print("El jugador ", jugador2.name, " ha sido eliminado.")
            if danoPorCiclo == 0:
                print("Cerramos bucle")
                break
def peleaCartas(indexCardTurn, arrCardOfPlayer, arrCardDefPlayer, defPlayer):
    dano = 0
    if (arrCardOfPlayer[indexCardTurn].type == "infantry" and arrCardDefPlayer[indexCardTurn].type == "lancer"):
        if(arrCardOfPlayer[indexCardTurn].attack*2 >= arrCardDefPlayer[indexCardTurn].defense):
            dano = comparaAtaqueDefensa(indexCardTurn, arrCardOfPlayer[indexCardTurn], arrCardDefPlayer[indexCardTurn], defPlayer, arrCardDefPlayer, 2)
        return dano
    elif (arrCardOfPlayer[indexCardTurn].type == "lancer" and arrCardDefPlayer[indexCardTurn].type == "chivalry"):
        if (arrCardOfPlayer[indexCardTurn].attack * 2 >= arrCardDefPlayer[indexCardTurn].defense):
            dano = comparaAtaqueDefensa(indexCardTurn, arrCardOfPlayer[indexCardTurn], arrCardDefPlayer[indexCardTurn], defPlayer, arrCardDefPlayer, 2)
        return dano
    elif (arrCardOfPlayer[indexCardTurn].type == "chivalry" and arrCardDefPlayer[indexCardTurn].type == "infantry"):
        if (arrCardOfPlayer[indexCardTurn].attack * 2 >= arrCardDefPlayer[indexCardTurn].defense):
            dano = comparaAtaqueDefensa(indexCardTurn, arrCardOfPlayer[indexCardTurn], arrCardDefPlayer[indexCardTurn], defPlayer, arrCardDefPlayer, 2)
        return dano
    else:
        if (arrCardOfPlayer[indexCardTurn].attack >= arrCardDefPlayer[indexCardTurn].defense):
            dano = comparaAtaqueDefensa(indexCardTurn, arrCardOfPlayer[indexCardTurn], arrCardDefPlayer[indexCardTurn], defPlayer, arrCardDefPlayer, 1)
        return dano

def comparaAtaqueDefensa(indexCardTurn, ofCard, defCard, defPlayer, arrCardDefPlayer, modificador):
    print("********* COMPARA ATATQUE Y DEF ***********")
    print(indexCardTurn)
    print(ofCard)
    print(defCard)
    print(defPlayer)
    print(arrCardDefPlayer[indexCardTurn])
    print(modificador)
    print(ofCard.attack)
    print(defCard.defense)
    print(int(defCard.defense) - (int(ofCard.attack)*modificador))
    dano = int(defCard.defense) - (int(ofCard.attack)*modificador)
    defPlayer.life = defPlayer.life - abs(dano)
    print("Vida despues de comabte", defPlayer.life)
    print("La carta del jugador ", defPlayer.name, " ", arrCardDefPlayer[indexCardTurn].name, " ha sido eliminida")
    del arrCardDefPlayer[indexCardTurn]
    return dano

confrontacion(jugador1, jugador2)

