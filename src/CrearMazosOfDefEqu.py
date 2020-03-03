import xml.etree.ElementTree as ALL
import array
tree = ALL.parse('xml_dtd/myBaraja.xml')
rootXml = tree.getroot()
from src.Card import Card

#Bucle para seleccionar las diez cartas con mayor ataque usando Xpath
#Se seleccionan primero todas las cartas de ataque 5, luego 4, luego 3....asi hasta haber seleccionando 10 cartas
def arrOfCards(XmlElement):
    numCartasAttack = 0
    maxAttack = 5
    arrCards = []

    while numCartasAttack < 10:
        for card in XmlElement.findall("./deck/card/[attack='"+str(maxAttack)+"']"):
            #print(ALL.tostring(card, encoding='utf8').decode('utf8')) para visualizar lo que fue selecionado
            carta=Card(card.attrib['summonPoints'],card.attrib['type'],card.find('name').text,card.find('description').text,card.find('attack').text,card.find('defense').text)
            arrCards.append(carta)
            numCartasAttack = numCartasAttack + 1
            if numCartasAttack == 10:
                break
        maxAttack = maxAttack - 1

    return arrCards

#Bucle para seleccionar las diez cartas con mayor defensa usando Xpath
#Se seleccionan primero todas las cartas de defensa 5, luego 4, luego 3....asi hasta haber seleccionando 10 cartas
def arrDefCards(XmlElement):
    numCartasDefense = 0
    maxDefense = 5
    arrCards = []
    while numCartasDefense < 10:
        for card in XmlElement.findall("./deck/card/[defense='"+str(maxDefense)+"']"):
            # print(ALL.tostring(card, encoding='utf8').decode('utf8')) para visualizar lo que fue selecionado
            numCartasDefense = numCartasDefense + 1
            carta = Card(card.attrib['summonPoints'], card.attrib['type'], card.find('name').text, card.find('description').text, card.find('attack').text, card.find('defense').text)
            arrCards.append(carta)
            if numCartasDefense == 10:
                break
        maxDefense = maxDefense - 1
    return arrCards

#Bucle para seleccionar las diez cartas con menor diferencia entre ataque y defensa usando Xpath
#Se seleccionan primero todas las cartas de diferencia entre ataque y defensa igual a 0, luego 1, luego 2....asi hasta haber seleccionando 10 cartas
def arrEqCards(XmlElement):

    numCartasEquilibrado = 0
    diferenciaAttDef = 0
    arrCards = []

    while numCartasEquilibrado < 10:
        for card in XmlElement.findall("./deck/card"):
            attack = int(card.find('attack').text)
            defense = int(card.find('defense').text)
            if abs(attack - defense) == diferenciaAttDef:
                # print(ALL.tostring(card, encoding='utf8').decode('utf8')) para visualizar lo que fue selecionado
                numCartasEquilibrado = numCartasEquilibrado + 1
                carta = Card(card.attrib['summonPoints'], card.attrib['type'], card.find('name').text, card.find('description').text, card.find('attack').text, card.find('defense').text)
                arrCards.append(carta)
                if numCartasEquilibrado == 10:
                    break
        diferenciaAttDef = diferenciaAttDef + 1
    return arrCards

