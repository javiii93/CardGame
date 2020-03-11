from src.Player import Player

def CrearJugadores():
    arrPlayer = []
    print("Cantidad de jugadores que van a jugar:")
    cantJugadores = int(input())
    for h in range(0, cantJugadores):
        print("Introduce el nombre del jugador ", h, ":")
        arrPlayer.append(Player(input()))
    return arrPlayer
