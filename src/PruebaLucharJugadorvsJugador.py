#lista de diccionarios Python
import xml.etree.ElementTree as ALL
from random import randint

from src.Card import Card
from src.MazoAleatorio import arrRandomCards
from src.Player import Player

#tree = ALL.parse('xml_dtd/myBaraja.xml')
#rootPlayer = tree.getroot()

#Creacino de los mazos aleatorios para probar el alogoritmo
#arrCard1 = arrRandomCards(rootPlayer)
#arrCard2 = arrRandomCards(rootPlayer)

#Dos jugadores de prueba con los mazos creados anteriormente asociados
#jugador1 = Player('Jugador1', arrCard1)
#jugador2 = Player('Jugador2', arrCard2)

#Mostramos las cartas de los mazos de los dos jugadores
#print("Cartas mazo jugador 1 :")
#for h in range(len(jugador1.arrCards)):
#    print(jugador1.arrCards[h])
#print("Cartas mazo jugador 2 :")
#for h in range(len(jugador2.arrCards)):
#    print(jugador2.arrCards[h])

#print()
#print()

#DEFINICION DE FUNCIONES UTILIZADAS POR EL ALGORITMO

#Funcion para crear un array des diez posiciones que contagan aleatoriamente valores entre 0 y 9 (cada mazo lleva 10 cartas)
def randomNumArray10():
    arr = []
    for i in range(10):
        value = randint(0, 9)
        # Hay que comprobar si el nuevo numero aleatorio esta en el array.
        while (value in arr):
            value = randint(0, 9)
        arr.append(value)
    return arr

#Funcion crear las cartas de mano de un jugador para un turno. Escoger cartas aleaoriamente hasta consumir los cinco
#puntos de invocacion de que tiene el jugador por turno
def invocacion(jugador):
    #reiniciar puntos de invocacion del jugador a 5
    jugador.summonPoints = 5
    #Crear array de las cartas del turno
    arrCardTurnPlayer = []
    #seleccionar cartas aleatorias del mazo hasta agotar puntos de invocacion e ir metiendo las cartas en el array de cartas del turno
    randomArray = randomNumArray10()
    arrayIndex = 0
    while jugador.summonPoints > 0 and arrayIndex < 10:
        if (jugador.summonPoints - int(jugador.arrCards[randomArray[arrayIndex]].summonPoints)) >= 0:
            jugador.summonPoints = jugador.summonPoints - int(jugador.arrCards[randomArray[arrayIndex]].summonPoints)
            arrCardTurnPlayer.append((jugador.arrCards[randomArray[arrayIndex]]))
        arrayIndex = arrayIndex + 1
    return arrCardTurnPlayer

#Funcion para tira aleatoriamente 1 o 2 para luego escoger que jugador empieza primero (jugador1 es el jugador
#metido en parametro primero en la funcion confrontacion. El jugador2 es el que es metido en segundo.
def destino():
    value = randint(1,2)
    return value

#Funcion para hacer la pelae entre las cartas de los jugadores. Es equivalente a un ciclo. Un turno puede tener varios ciclos.
#El ciclo acaba cuando se dejan de cumplir las condiciones especificadas por los ucles while o cuando se dejen de hacer dano
#entre las cartas (por ejemplo: solo hay cartas defensivas sin ataque en juego -> el juego se bloquea y se termina el turno
#por lo cual se vuelve a empezar desde la fase invocacion (nuevo turno)
def confrontacion(jugador1, jugador2, arrCardTurnPlayer1, arrCardTurnPlayer2): #parametros : jugador local y jugador enemigo
    valorDestino = destino()
    if valorDestino == 1:#el jugador1 atacara primero
        while jugador1.life > 0 and jugador2.life > 0 and len(arrCardTurnPlayer1) > 0 and len(arrCardTurnPlayer2) > 0:
            danoPorCiclo = 0 #a cada ciclo se reinicializa danoPorCiclo
            for indexCardTurn in range(0,len(arrCardTurnPlayer1)): #Recorremos cada carta de la mano del jugador ofensivo para atacar
                if indexCardTurn < len(arrCardTurnPlayer2):#si el jugador defensivo tiene una carta para defenderse se hace la pelea
                                                           #entre las cartas
                    danoPorCiclo = danoPorCiclo + peleaCartas(indexCardTurn, arrCardTurnPlayer1, arrCardTurnPlayer2, jugador2)
                else:#si el jugador defensivo no tiene cartas para defenderse se le restan los puntos de ataque de la
                     #ofensiva directamente a sus puntos de vida
                    jugador2.life = int(jugador2.life) - int(arrCardTurnPlayer1[indexCardTurn].attack)
            if jugador2.life > 0:#si el jugador defensivo sigue vivo, le toca atacar
                for indexCardTurn in range(0,len(arrCardTurnPlayer2)):#Recorremos cada carta de la mano del jugador ofensivo para atacar
                    if indexCardTurn < len(arrCardTurnPlayer1):#si el jugador defensivo tiene una carta para defenderse se hace la pelea
                                                               #entre las cartas
                        danoPorCiclo = danoPorCiclo + peleaCartas(indexCardTurn, arrCardTurnPlayer2, arrCardTurnPlayer1, jugador1)
                    else:#si el jugador defensivo no tiene cartas para defenderse se le restan los puntos de ataque de la
                         #ofensiva directamente a sus puntos de vida
                        jugador1.life = int(jugador1.life) - int(arrCardTurnPlayer2[indexCardTurn].attack)
            if jugador1.life <= 0:
                print("El jugador ", jugador1.name, " ha sido eliminado.")
            if jugador2.life <= 0:
                print("El jugador ", jugador2.name, " ha sido eliminado.")
            if danoPorCiclo == 0: #si no han habido peleas de cartas con danos cerramos el turno
                break
        print("Danos totales recibidos por el jugador ", jugador1.name, " ", 10 - jugador1.life)
        print("Danos totales recibidos por el jugador ", jugador2.name, " ", 10 - jugador2.life)

    if valorDestino == 2:#el jugador2 atacara primero
        while jugador1.life > 0 and jugador2.life > 0 and len(arrCardTurnPlayer1) > 0 and len(arrCardTurnPlayer2) > 0:
            danoPorCiclo = 0 #a cada ciclo se reinicializa danoPorCiclo
            for indexCardTurn in range(0,len(arrCardTurnPlayer2)):#Recorremos cada carta de la mano del jugador ofensivo para atacar
                if indexCardTurn < len(arrCardTurnPlayer1):#si el jugador defensivo tiene una carta para defenderse se hace la pelea
                                                           #entre las cartas
                    danoPorCiclo = danoPorCiclo + peleaCartas(indexCardTurn, arrCardTurnPlayer2, arrCardTurnPlayer1, jugador1)
                else:#si el jugador defensivo no tiene cartas para defenderse se le restan los puntos de ataque de la
                     #ofensiva directamente a sus puntos de vida
                    jugador1.life = int(jugador1.life) - int(arrCardTurnPlayer2[indexCardTurn].attack)
            if jugador1.life > 0:#si el jugador defensivo sigue vivo, le toca atacar
                for indexCardTurn in range(0,len(arrCardTurnPlayer1)):#Recorremos cada carta de la mano del jugador ofensivo para atacar
                    if indexCardTurn < len(arrCardTurnPlayer2):#si el jugador defensivo tiene una carta para defenderse se hace la pelea
                                                               #entre las cartas
                       danoPorCiclo = danoPorCiclo + peleaCartas(indexCardTurn, arrCardTurnPlayer1, arrCardTurnPlayer2, jugador2)
                    else:#si el jugador defensivo no tiene cartas para defenderse se le restan los puntos de ataque de la
                         #ofensiva directamente a sus puntos de vida
                        jugador2.life = int(jugador2.life) - int(arrCardTurnPlayer1[indexCardTurn].attack)
            if jugador1.life <= 0:
                print("El jugador ", jugador1.name, " ha sido eliminado.")
            if jugador2.life <= 0:
                print("El jugador ", jugador2.name, " ha sido eliminado.")
            if danoPorCiclo == 0:#si no han habido peleas de cartas con danos cerramos el turno
                break
        print("Danos totales recibidos por el jugador ", jugador1.name, " ", 10 - jugador1.life)
        print("Danos totales recibidos por el jugador ", jugador2.name, " ", 10 - jugador2.life)

#Funcion para hacer la pelea entre las cartas aplicando un modificador de ataque segun el tipo de carta ofensiva y defensiva
def peleaCartas(indexCardTurn, arrCardOfPlayer, arrCardDefPlayer, defPlayer):
    dano = 0
    # infantry vs lancer -> modificador de ataque por 2 a infantry
    if (arrCardOfPlayer[indexCardTurn].type == "infantry" and arrCardDefPlayer[indexCardTurn].type == "lancer"):
        # si el ataque resultante es superior a la defensa de la carta defensiva entenonces se elimina la carta defensiva
        #y los puntos restante se restan a la vida del jugador defensivo (funcion comparaAtaqueDefensa). Si la defensa
        #es superior al ataque no pasa nada. Mismo comentario para las otras situaciones.
        if(arrCardOfPlayer[indexCardTurn].attack*2 > arrCardDefPlayer[indexCardTurn].defense):
            dano = comparaAtaqueDefensa(indexCardTurn, arrCardOfPlayer[indexCardTurn], arrCardDefPlayer[indexCardTurn], defPlayer, arrCardDefPlayer, 2)
        return dano
    # lancer vs chivalry -> modificador de ataque por 2 a lancer
    elif (arrCardOfPlayer[indexCardTurn].type == "lancer" and arrCardDefPlayer[indexCardTurn].type == "chivalry"):
        if (arrCardOfPlayer[indexCardTurn].attack * 2 > arrCardDefPlayer[indexCardTurn].defense):
            dano = comparaAtaqueDefensa(indexCardTurn, arrCardOfPlayer[indexCardTurn], arrCardDefPlayer[indexCardTurn], defPlayer, arrCardDefPlayer, 2)
        return dano
    # chivalry vs infantry -> modificador de ataque por 2 a chivalry
    elif (arrCardOfPlayer[indexCardTurn].type == "chivalry" and arrCardDefPlayer[indexCardTurn].type == "infantry"):
        if (arrCardOfPlayer[indexCardTurn].attack * 2 > arrCardDefPlayer[indexCardTurn].defense):
            dano = comparaAtaqueDefensa(indexCardTurn, arrCardOfPlayer[indexCardTurn], arrCardDefPlayer[indexCardTurn], defPlayer, arrCardDefPlayer, 2)
        return dano
    # en los otros casos el modificador es 1
    else:
        if (arrCardOfPlayer[indexCardTurn].attack > arrCardDefPlayer[indexCardTurn].defense):
            dano = comparaAtaqueDefensa(indexCardTurn, arrCardOfPlayer[indexCardTurn], arrCardDefPlayer[indexCardTurn], defPlayer, arrCardDefPlayer, 1)
        return dano

#Funcion para eleminar la carta defensiva y restar los puntos sobretantes del ataque de la carta ofensiva a la vida
#del jugador ofensivo
def comparaAtaqueDefensa(indexCardTurn, ofCard, defCard, defPlayer, arrCardDefPlayer, modificador):
    dano = int(defCard.defense) - (int(ofCard.attack)*modificador)
    defPlayer.life = defPlayer.life - abs(dano)
    print("La carta del jugador ", defPlayer.name, " ", arrCardDefPlayer[indexCardTurn].name, " ha sido eliminida")
    del arrCardDefPlayer[indexCardTurn]
    return dano



# EJECUCION DE LAS FUNCIONES
def ejecutarPartida(jugador1, jugador2):
    turno = 1
    while jugador1.life > 0 and jugador2.life > 0:
        print("******** TURNO ", turno, "********" )
        #A cada jugador se le asocia unas cartas de turno a partir de su mazo
        arrCardTurnPlayer1 = invocacion(jugador1)
        arrCardTurnPlayer2 = invocacion(jugador2)

        #Mostramos las cartas de mano de turno de cada jugador
        print("cartas turno jugador 1 :")
        for h in range(len(arrCardTurnPlayer1)):
            print(arrCardTurnPlayer1[h])
        print("cartas turno jugador 2 :")
        for h in range(len(arrCardTurnPlayer2)):
            print(arrCardTurnPlayer2[h])

        print()
        print()

        confrontacion(jugador1, jugador2, arrCardTurnPlayer1, arrCardTurnPlayer2)

        turno = turno + 1

        print()

    if jugador1.life > 0:
        jugador1.victoryPoints = jugador1.victoryPoints + 20
    elif jugador2.life > 0:
        jugador2.victoryPoints = jugador2.victoryPoints + 20

def ligaSantander(arrPlayers):
    if not arrPlayers or len(arrPlayers) <= 1:
        print("List is empty or list got just 1 player")
    else:
        for h in range(len(arrPlayers)):
            for i in range(len(arrPlayers)):
                if (not arrPlayers[h] == arrPlayers[i]):
                    ejecutarPartida(arrPlayers[h], arrPlayers[i])