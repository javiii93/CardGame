class Player:
    def __init__(self, _name, _arrCardsP=None):
        self.summonPoints = 5
        self.life = 10
        self.arrCards = _arrCardsP
        self.name = _name
        self.victoryPoints = 0

    def __str__(self):
        return "Name: " + str(self.name) + ", Life: " + str(self.life)+ ", SummonPoints: " + str(self.summonPoints)

    def __eq__(self, other):
        if not isinstance(other, Player):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.name == other.name and self.arrCards == other.arrCards