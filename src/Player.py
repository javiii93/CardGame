class Player:
    def __init__(self, _name, _arrCardsP=None):
        self.summonPoints = 5
        self.life = 10
        self.arrCards = _arrCardsP
        self.name=_name

    def __str__(self):
        return "Name: " + str(self.name) + ", Life: " + str(self.life)+ ", SummonPoints: " + str(self.summonPoints)

