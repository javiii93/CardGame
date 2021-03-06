import xml.etree.ElementTree as ALL


# https://docs.python.org/2/library/xml.etree.elementtree.html

def cardsPrint(arg):
    for card in arg.findall('./deck/card'):
        att = card.attrib
        name = card.find('name').text
        desc = card.find('description').text
        attack = card.find('attack').text
        defense = card.find('defense').text
        print(att, "Name=", name, "Description=", desc, "Attack=", attack, "Defense=", defense)


def treeLoad(arg):
    if (arg is None):
        print("Can't load tree")
    else:
        print("Load tree succesfully")


def loadXml(arg):
    tree = ALL.parse(arg)
    rootXml = tree.getroot()
    return rootXml
