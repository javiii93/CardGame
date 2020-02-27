import xml.etree.ElementTree as ALL

tree = ALL.parse('xml_dtd/myBaraja.xml')
rootXml = tree.getroot()

#Bucle para seleccionar las diez cartas con mayor ataque usando Xpath

numCartasAttack = 0
maxAttack = 5


while numCartasAttack < 10:
    for card in rootXml.findall("./deck/card/[attack='"+str(maxAttack)+"']"):
        #print(ALL.tostring(card, encoding='utf8').decode('utf8')) para visualizar lo que fue selecionado
        # a remplzar por signacion a objeto
        numCartasAttack = numCartasAttack + 1
        if numCartasAttack == 10:
            break
    maxAttack = maxAttack - 1

print("*********")

numCartasDefense = 0
maxDefense = 5

#Bucle para seleccionar las diez cartas con mayor defensa usando Xpath

while numCartasDefense < 10:
    for card in rootXml.findall("./deck/card/[defense='"+str(maxDefense)+"']"):
        # print(ALL.tostring(card, encoding='utf8').decode('utf8')) para visualizar lo que fue selecionado
        # a remplzar por signacion a objeto
        numCartasDefense = numCartasDefense + 1
        if numCartasDefense == 10:
            break
    maxDefense = maxDefense - 1

print("*********")

#Bucle para seleccionar las diez cartas con menor diferencia entre ataque y defensa usando Xpath

numCartasEquilibrado = 0
diferenciaAttDef = 0

while numCartasEquilibrado < 10:
    for card in rootXml.findall("./deck/card"):
        attack = int(card.find('attack').text)
        defense = int(card.find('defense').text)
        if abs(attack - defense) == diferenciaAttDef:
            # print(ALL.tostring(card, encoding='utf8').decode('utf8')) para visualizar lo que fue selecionado
            # a remplzar por signacion a objeto
            numCartasEquilibrado = numCartasEquilibrado + 1
            if numCartasEquilibrado == 10:
                break
    diferenciaAttDef = diferenciaAttDef + 1

