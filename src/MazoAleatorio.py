import xml.etree.ElementTree as ALL
from random import sample, randrange

tree = ALL.parse('xml_dtd/myBaraja.xml')
rootXml = tree.getroot()

numCartas = 0;






while numCartas < 10:
    numero = randrange(5)
    print (numero)
    for card in rootXml.findall("./deck/card[@summonPoints='"+str(numero)+"']"):
        print(ALL.tostring(card, encoding='utf8').decode('utf8'))
        numCartas = numCartas + 1
        break
        if numCartas == 10:
            break


print("*********")
