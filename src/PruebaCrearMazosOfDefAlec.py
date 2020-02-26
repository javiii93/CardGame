import xml.etree.ElementTree as ALL

tree = ALL.parse('xml_dtd/myBaraja.xml')
rootXml = tree.getroot()

numCartasAttack = 0
maxAttack = 5


while numCartasAttack < 10:
    for card in rootXml.findall("./deck/card/[attack='"+str(maxAttack)+"']"):
        print(ALL.tostring(card, encoding='utf8').decode('utf8'))
        numCartasAttack = numCartasAttack + 1
        if numCartasAttack == 10:
            break
    maxAttack = maxAttack - 1

print("*********")

numCartasDefense = 0
maxDefense = 5


while numCartasDefense < 10:
    for card in rootXml.findall("./deck/card/[defense='"+str(maxDefense)+"']"):
        print(ALL.tostring(card, encoding='utf8').decode('utf8'))
        numCartasDefense = numCartasDefense + 1
        if numCartasDefense == 10:
            break
    maxDefense = maxDefense - 1

