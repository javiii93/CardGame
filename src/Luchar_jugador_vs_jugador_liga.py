#lista de diccionarios Python
import xml.etree.ElementTree as ALL
from random import randint
from src.Luchar_jugador_vs_jugador import randomNumArray10, destino
from src.Card import Card
from src.MazoAleatorio import arrRandomCards
from src.Player import Player

tree = ALL.parse('xml_dtd/myBaraja.xml')
rootPlayer = tree.getroot()

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

#DEFINICION DE FUNCIONES UTILIZADAS POR EL ALGORITMO DE LUCHA LIGA


#Funcion crear las cartas de mano de un jugador para un turno. Escoger cartas aleaoriamente hasta consumir los cinco
#puntos de invocacion de que tiene el jugador por turno
from src.PruebasVarias import archivoJornadas, archivoClasificaciones


def invocacionLiga(jugador):
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

#Funcion para hacer la pelae entre las cartas de los jugadores. Es equivalente a un ciclo. Un turno puede tener varios ciclos.
#El ciclo acaba cuando se dejan de cumplir las condiciones especificadas por los ucles while o cuando se dejen de hacer dano
#entre las cartas (por ejemplo: solo hay cartas defensivas sin ataque en juego -> el juego se bloquea y se termina el turno
#por lo cual se vuelve a empezar desde la fase invocacion (nuevo turno)
def confrontacionLiga(jugador1, jugador2, arrCardTurnPlayer1, arrCardTurnPlayer2): #parametros : jugador local y jugador enemigo
    valorDestino = destino()
    if valorDestino == 1:#el jugador1 atacara primero
        while jugador1.life > 0 and jugador2.life > 0 and len(arrCardTurnPlayer1) > 0 and len(arrCardTurnPlayer2) > 0:
            danoPorCiclo = 0 #a cada ciclo se reinicializa danoPorCiclo
            for indexCardTurn in range(0,len(arrCardTurnPlayer1)): #Recorremos cada carta de la mano del jugador ofensivo para atacar
                if indexCardTurn < len(arrCardTurnPlayer2):#si el jugador defensivo tiene una carta para defenderse se hace la pelea
                                                           #entre las cartas
                    danoPorCiclo = danoPorCiclo + peleaCartasLiga(indexCardTurn, arrCardTurnPlayer1, arrCardTurnPlayer2, jugador2)
                else:#si el jugador defensivo no tiene cartas para defenderse se le restan los puntos de ataque de la
                     #ofensiva directamente a sus puntos de vida
                    jugador2.life = int(jugador2.life) - int(arrCardTurnPlayer1[indexCardTurn].attack)
            if jugador2.life > 0:#si el jugador defensivo sigue vivo, le toca atacar
                for indexCardTurn in range(0,len(arrCardTurnPlayer2)):#Recorremos cada carta de la mano del jugador ofensivo para atacar
                    if indexCardTurn < len(arrCardTurnPlayer1):#si el jugador defensivo tiene una carta para defenderse se hace la pelea
                                                               #entre las cartas
                        danoPorCiclo = danoPorCiclo + peleaCartasLiga(indexCardTurn, arrCardTurnPlayer2, arrCardTurnPlayer1, jugador1)
                    else:#si el jugador defensivo no tiene cartas para defenderse se le restan los puntos de ataque de la
                         #ofensiva directamente a sus puntos de vida
                        jugador1.life = int(jugador1.life) - int(arrCardTurnPlayer2[indexCardTurn].attack)
            if danoPorCiclo == 0: #si no han habido peleas de cartas con danos cerramos el turno
                break

    if valorDestino == 2:#el jugador2 atacara primero
        while jugador1.life > 0 and jugador2.life > 0 and len(arrCardTurnPlayer1) > 0 and len(arrCardTurnPlayer2) > 0:
            danoPorCiclo = 0 #a cada ciclo se reinicializa danoPorCiclo
            for indexCardTurn in range(0,len(arrCardTurnPlayer2)):#Recorremos cada carta de la mano del jugador ofensivo para atacar
                if indexCardTurn < len(arrCardTurnPlayer1):#si el jugador defensivo tiene una carta para defenderse se hace la pelea
                                                           #entre las cartas
                    danoPorCiclo = danoPorCiclo + peleaCartasLiga(indexCardTurn, arrCardTurnPlayer2, arrCardTurnPlayer1, jugador1)
                else:#si el jugador defensivo no tiene cartas para defenderse se le restan los puntos de ataque de la
                     #ofensiva directamente a sus puntos de vida
                    jugador1.life = int(jugador1.life) - int(arrCardTurnPlayer2[indexCardTurn].attack)
            if jugador1.life > 0:#si el jugador defensivo sigue vivo, le toca atacar
                for indexCardTurn in range(0,len(arrCardTurnPlayer1)):#Recorremos cada carta de la mano del jugador ofensivo para atacar
                    if indexCardTurn < len(arrCardTurnPlayer2):#si el jugador defensivo tiene una carta para defenderse se hace la pelea
                                                               #entre las cartas
                       danoPorCiclo = danoPorCiclo + peleaCartasLiga(indexCardTurn, arrCardTurnPlayer1, arrCardTurnPlayer2, jugador2)
                    else:#si el jugador defensivo no tiene cartas para defenderse se le restan los puntos de ataque de la
                         #ofensiva directamente a sus puntos de vida
                        jugador2.life = int(jugador2.life) - int(arrCardTurnPlayer1[indexCardTurn].attack)

            if danoPorCiclo == 0:#si no han habido peleas de cartas con danos cerramos el turno
                break

#Funcion para hacer la pelea entre las cartas aplicando un modificador de ataque segun el tipo de carta ofensiva y defensiva
def peleaCartasLiga(indexCardTurn, arrCardOfPlayer, arrCardDefPlayer, defPlayer):
    dano = 0
    # infantry vs lancer -> modificador de ataque por 2 a infantry
    if (arrCardOfPlayer[indexCardTurn].type == "infantry" and arrCardDefPlayer[indexCardTurn].type == "lancer"):
        # si el ataque resultante es superior a la defensa de la carta defensiva entenonces se elimina la carta defensiva
        #y los puntos restante se restan a la vida del jugador defensivo (funcion comparaAtaqueDefensa). Si la defensa
        #es superior al ataque no pasa nada. Mismo comentario para las otras situaciones.
        if(arrCardOfPlayer[indexCardTurn].attack*2 >= arrCardDefPlayer[indexCardTurn].defense):
            dano = comparaAtaqueDefensaLiga(indexCardTurn, arrCardOfPlayer[indexCardTurn], arrCardDefPlayer[indexCardTurn], defPlayer, arrCardDefPlayer, 2)
        return dano
    # lancer vs chivalry -> modificador de ataque por 2 a lancer
    elif (arrCardOfPlayer[indexCardTurn].type == "lancer" and arrCardDefPlayer[indexCardTurn].type == "chivalry"):
        if (arrCardOfPlayer[indexCardTurn].attack * 2 >= arrCardDefPlayer[indexCardTurn].defense):
            dano = comparaAtaqueDefensaLiga(indexCardTurn, arrCardOfPlayer[indexCardTurn], arrCardDefPlayer[indexCardTurn], defPlayer, arrCardDefPlayer, 2)
        return dano
    # chivalry vs infantry -> modificador de ataque por 2 a chivalry
    elif (arrCardOfPlayer[indexCardTurn].type == "chivalry" and arrCardDefPlayer[indexCardTurn].type == "infantry"):
        if (arrCardOfPlayer[indexCardTurn].attack * 2 >= arrCardDefPlayer[indexCardTurn].defense):
            dano = comparaAtaqueDefensaLiga(indexCardTurn, arrCardOfPlayer[indexCardTurn], arrCardDefPlayer[indexCardTurn], defPlayer, arrCardDefPlayer, 2)
        return dano
    # en los otros casos el modificador es 1
    else:
        if (arrCardOfPlayer[indexCardTurn].attack >= arrCardDefPlayer[indexCardTurn].defense):
            dano = comparaAtaqueDefensaLiga(indexCardTurn, arrCardOfPlayer[indexCardTurn], arrCardDefPlayer[indexCardTurn], defPlayer, arrCardDefPlayer, 1)
        return dano

#Funcion para eleminar la carta defensiva y restar los puntos sobretantes del ataque de la carta ofensiva a la vida
#del jugador ofensivo
def comparaAtaqueDefensaLiga(indexCardTurn, ofCard, defCard, defPlayer, arrCardDefPlayer, modificador):
    dano = int(defCard.defense) - (int(ofCard.attack)*modificador)
    defPlayer.life = defPlayer.life - abs(dano)
    del arrCardDefPlayer[indexCardTurn]
    return dano



# EJECUCION DE LAS FUNCIONES
def ejecutarPartidaLiga(jugador1, jugador2, ficheroJornada):
    jugador1.life = 10
    jugador2.life = 10
    turno = 1
    while jugador1.life > 0 and jugador2.life > 0:
        #A cada jugador se le asocia unas cartas de turno a partir de su mazo
        arrCardTurnPlayer1 = invocacionLiga(jugador1)
        arrCardTurnPlayer2 = invocacionLiga(jugador2)

        #Mostramos las cartas de mano de turno de cada jugador
        #print("cartas turno jugador 1 :")
        #for h in range(len(arrCardTurnPlayer1)):
        #   print(arrCardTurnPlayer1[h])
        #print("cartas turno jugador 2 :")
        #for h in range(len(arrCardTurnPlayer2)):
        #    print(arrCardTurnPlayer2[h])

        #print()
        #print()

        confrontacionLiga(jugador1, jugador2, arrCardTurnPlayer1, arrCardTurnPlayer2)

        turno = turno + 1

        #print()
    if jugador1.life <= 0:
        print("El jugador ", jugador2.name, " ha ganado la partida.")
        resultado = "El jugador "+jugador2.name+" ha ganado la partida."
        archivoJornadas(ficheroJornada, resultado)
        print("jugador 1 life :", jugador1.life)
        print("jugador 2 life :", jugador2.life)
    if jugador2.life <= 0:
        print("El jugador ", jugador1.name, " ha ganado la partida.")
        resultado = "El jugador "+jugador1.name+" ha ganado la partida."
        archivoJornadas(ficheroJornada, resultado)
        print("jugador 1 life :", jugador1.life)
        print("jugador 2 life :", jugador2.life)
    if jugador1.life > 0:
        jugador1.victoryPoints = jugador1.victoryPoints + 20
    elif jugador2.life > 0:
        jugador2.victoryPoints = jugador2.victoryPoints + 20

def ligaSantander(arrPlayers, ficheroJornada, ficheroClasificacion):
    def numerosCombinatorios(n, k):
        if k == 0:
            return 1
        elif n == 0:
            return 0
        else:
            return numerosCombinatorios(n - 1, k - 1) + numerosCombinatorios(n - 1, k)

    total = numerosCombinatorios(6, 2)

    matrice = [[]] * total

    for i in range(len(matrice)):
        matrice[i] = [0] * 2

    # for i in range(len(matrice)):
    #    print(matrice[i])

    def partidos_aleatorios():
        i = 0
        while i < len(matrice):
            partidoHecho = False

            while partidoHecho == False:

                jugador1 = 0
                jugador2 = 0
                while jugador1 == jugador2:
                    jugador1 = randint(0, 5)
                    jugador2 = randint(0, 5)

                for j in range(len(matrice)):
                    if (jugador1 == matrice[j][0] and jugador2 == matrice[j][1]) or (
                            jugador1 == matrice[j][1] and jugador2 == matrice[j][0]):
                        partidoHecho = True
                        break

                if partidoHecho == False:
                    matrice[i][0] = jugador1
                    matrice[i][1] = jugador2
                    i = i + 1


    for i in range(len(matrice)):
        print(matrice[i])

    for i in range(len(arrPlayers)):
        for j in range(len(arrPlayers[i].arrCards)):
            print(arrPlayers[i].arrCards[j])
        print()

    partidos_aleatorios()

    for i in range(len(matrice)):
        print(matrice[i])

    for i in range(len(matrice)):
        print(matrice[i][0])
        print(matrice[i][1])
        print()
        #arrPlayers(matrice[i][0]).life = 10
        #arrPlayers(matrice[i][1]).life = 10
        ejecutarPartidaLiga(arrPlayers[matrice[i][0]], arrPlayers[matrice[i][1]], ficheroJornada)