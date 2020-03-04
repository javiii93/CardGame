from src.Card import Card
from src.Main import rootPlayer
from src.MazoAleatorio import arrRandomCards
from src.Player import Player

arrCardPlayer = arrRandomCards(rootPlayer)
Jugador = Player('Sergio', arrCardPlayer);
print(Player.life);
print('Hola')

def PlayerVsBot(arrCardPlayer, arrCardEnemy):
    Jugador = Player('Sergio', arrCardPlayer);
    print(Jugador.life);
    print('Hola')