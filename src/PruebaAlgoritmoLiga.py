#Numeros combinatorios
from random import randint


def numerosCombinatorios(n, k):
    if k == 0 :
        return 1
    elif n == 0 :
        return 0
    else:
        return numerosCombinatorios(n-1, k-1) + numerosCombinatorios(n-1, k)

total = numerosCombinatorios(6, 2)


matrice = [[]]*total

for i in range(len(matrice)):
    matrice[i] = [0]*2

#for i in range(len(matrice)):
#    print(matrice[i])

def x():
    i = 0
    while i < len(matrice):
        partidoHecho = False

        while partidoHecho == False:

            jugador1 = 0
            jugador2 = 0
            while jugador1 == jugador2:
                jugador1 = randint(1, 6)
                jugador2 = randint(1, 6)

            for j in range(len(matrice)):
                    if (jugador1 == matrice[j][0] and jugador2 == matrice[j][1]) or (jugador1 == matrice[j][1] and jugador2 == matrice[j][0]):
                        partidoHecho = True
                        break

            if partidoHecho == False:
                matrice[i][0] = jugador1
                matrice[i][1] = jugador2
                i = i + 1



#print()
#matrice[5][1] = 10
#for i in range(len(matrice)):
#    print(matrice[i])
x()


for i in range(len(matrice)):
    print(matrice[i])