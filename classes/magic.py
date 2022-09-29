import random


class Spell:
    def __init__(self, name, cost, dmg, typee):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.typee = typee

    def generate_dmg(self, person):
        low = self.dmg - 3 + int((person.get_char_level()-1) * 1.65)
        high = self.dmg + 3 + int((person.get_char_level()-1) * 1.65)
        return random.randrange(low, high)
