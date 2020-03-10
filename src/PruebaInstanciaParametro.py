class jugadores:
    def __init__(self, _id, _nombre, _nivel):
        self.id = _id
        self.nombre = _nombre
        self.nivel = _nivel

    def __str__(self):
        return "id : " + str(self.id) + ", nombre : " + str(self.nombre) + ", nivel: " + str(
            self.nivel)


jugador1 = jugadores(1, "Juan", 2)
jugador2 = jugadores(2, "Maria", 3)

print(jugador1.__str__())
print(jugador2.__str__())

def modificarJugador(jugadores):
    jugadores.id = 3

modificarJugador(jugador1)
print(jugador1.__str__())

def modificarDosjugadores(jugador1, jugador2):
    jugador1.id = 10
    jugador2.id = 20

modificarDosjugadores(jugador1, jugador2)
print(jugador1.__str__())
print(jugador2.__str__())


if str(jugador1.nombre) == "Juan":
    print("*****")

dano = 0

while dano < 10:
    dano = dano + 1
    print(dano)

def ligaSantander(arrPlayers):
    if not arrPlayers or len(arrPlayers)<=1:
        print("List is empty or list got just 1 player")
    else:
        for h in range(len(arrPlayers)):
            for i in range(len(arrPlayers)):
                if(not arrPlayers[h]==arrPlayers[i]):
                    ejecutarPartida(arrPlayers[h], arrPlayers[i])   
