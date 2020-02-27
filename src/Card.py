class Card:
     def __init__(self, _summonPoints,_type,_name,_description,_attack,_defense):
        self.summonPoints = _summonPoints
        self.type = _type
        self.name = _name
        self.description = _description
        self.attack = _attack
        self.defense = _defense
     def __str__(self):
        return "summonPoints: ",self.summonPoints,", Type: ",self.type,", Name: ",self.name,", Description: ",self.description,", Attack: ",self.attack,", Defense: ",self.defense


x=Card(1,'fdsa','fsdaf','fdsfasd',4,4)
x.__str__()

