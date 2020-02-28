import xml.etree.ElementTree as ALL
from random import randint
tree = ALL.parse('xml_dtd/myBaraja.xml')
rootXml = tree.getroot()
numCartas = 1;


def randomNumArray():
    arr=[]
    for _ in range(10):
        value = randint(1, 20)
        #Hay que comprobar si el nuevo numero aleatorio esta en el array.
        while (value in arr):
            value = randint(1, 20)
        arr.append(value)
    return arr


array = randomNumArray()
#leer array de 10 numeros aleatorios y printear cartas aleatorias.
for i in range(len(array)):
   num = array[i]
   contador = 0
   while contador <= num:
       for card in rootXml.findall("./deck/card"):
           contador = contador + 1
           if contador == num:
               print(ALL.tostring(card, encoding='utf8').decode('utf8'))
               break