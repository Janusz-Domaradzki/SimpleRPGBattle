import random


class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

class Person:
    def __init__(self, level, hp, mp, atk, df, magic, name, party_color, items, xp_val):
        self.level = level - 1
        self.base_hp = hp
        self.base_mp = mp
        self.base_atk = atk
        self.maxhp = self.base_hp + int(self.level * 0.5 * self.base_hp) + int(self.level * 0.5)
        self.hp = self.maxhp
        self.maxmp = self.base_mp + int(self.level * 0.25 * self.base_mp) + int(self.level * 0.25)
        self.mp = self.maxmp
        self.atkl = self.base_atk - 2 + int(self.level * 1.2)
        self.atkh = self.base_atk + 2 + int(self.level * 1.2)
        self.df = df + int(self.level * 0.34)
        self.magic = magic
        self.action = ["Attack","Magic","Items"]
        self.name = name
        self.party_color = party_color
        self.items = items
        self.xp = 0
        self.maxxp = 10 + level * 7 + int(self.level * 0.85)
        self.base_xp = 10
        self.xp_val = xp_val

    def get_base(self, i):
        if i == "hp":
            return self.base_hp
        elif i == "mp":
            return self.base_mp
        elif i == "atk":
            return self.base_atk
        elif i == "xp":
            return self.base_xp
        else:
            print("error")
            return 44

    def generate_dmg(self):
        return random.randrange(self.atkl,self.atkh)

    def take_dmg(self,dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_xp(self):
        return self.xp

    def get_maxxp(self):
        return self.maxxp

    def get_xp_val(self):
        return self.xp_val

    def get_char_level(self):
        return self.level + 1

    def choose_action(self):
        i = 1
        print("Actions:")
        for item in self.action:
            print(str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("Magic:")
        if len(self.magic) < 1:
            print(" You don't have any magic")
            return -1
        else:
            for spell in self.magic:
                print(str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
                i += 1

    def choose_item(self):
        i = 1
        print("Items:")
        if len(self.items) < 1:
            print(" You don't have any items!")
            return -1
        else:
            for item in self.items:
                print(str(i) + ":", item.name, ".", item.description, "(")
                i += 1

    def print_stats(self):
        print("======= " + self.name + " =======")
        print("|| Lvl: " + str(self.get_char_level()) +
              " || XP: " + str(self.get_xp()) + "/" + str(self.get_maxxp()) + " ||\n" +
              "|| HP: " + self.party_color + str(self.get_hp()) + self.party_color + "/" + str(self.get_maxhp()) + bcolors.ENDC +
              " MP: " + bcolors.OKBLUE + str(self.get_mp()) + "/" + str(self.get_maxmp()) + bcolors.ENDC + " ||")

    def xp_increase(self, xp_gain):
        self.xp += xp_gain
        if self.xp > self.maxxp:
            self.xp = 0
            self.level += 1
            self.maxhp = self.get_base("hp") + int((self.get_char_level()-1) * 0.5 * self.get_base("hp")) + int(self.get_char_level() * 0.5)
            self.hp = self.get_maxhp()
            self.maxmp = self.get_base("mp") + int((self.get_char_level()-1) * 0.25 * self.get_base("mp")) + int(self.get_char_level() * 0.25)
            self.mp = self.get_maxmp()
            self.atkl = self.atkl + int((self.get_char_level()-1) * 1.2)
            self.atkh = self.atkh + int((self.get_char_level()-1) * 1.2)
            self.df = self.df + int(self.level * 0.34)
            self.maxxp = self.get_base("xp") + self.get_char_level() * 7 + int((self.get_char_level()-1) * 0.85)
            print("You've reached level " + str(self.get_char_level()) + "!!!")

