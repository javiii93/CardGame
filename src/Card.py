class Card:
     def __init__(self, _summonPoints,_type,_name,_description,_attack,_defense):
        self.summonPoints = _summonPoints
        self.type = _type
        self.name = _name
        self.description = _description
        self.attack = _attack
        self.defense = _defense
     def __str__(self):
        return "summonPoints: "+str(self.summonPoints)+", Type: "+str(self.type)+", Name: "+str(self.name)+", Description: "+str(self.description)+", Attack: "+str(self.attack)+", Defense: "+str(self.defense)


x=Card(1,'fdsa','fsdaf','fdsfasd',4,4)
print(x)

