import xml.etree.ElementTree as ALL
from random import randint

from src.Card import Card

tree = ALL.parse('xml_dtd/myBaraja.xml')
rootXml = tree.getroot()
numCartas = 1;


def randomNumArray():
    arr = []
    for _ in range(10):
        value = randint(1, 20)
        # Hay que comprobar si el nuevo numero aleatorio esta en el array.
        while (value in arr):
            value = randint(1, 20)
        arr.append(value)
    return arr


# leer array de 10 numeros aleatorios y printear cartas aleatorias.
def arrRandomCards(xmlElement):
    arrRandomNumber=randomNumArray()
    arrCards = []
    for i in range(len(arrRandomNumber)):
        num = arrRandomNumber[i]
        contador = 0
    while contador <= num:
        for card in rootXml.findall("./deck/card"):
            contador = contador + 1
            if contador == num:
                carta = Card(card.attrib['summonPoints'], card.attrib['type'], card.find('name').text,
                             card.find('description').text, card.find('attack').text, card.find('defense').text)
                arrCards.append(carta)
                print('carta añadida')
                break
    return arrCards
