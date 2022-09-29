from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

#create magic
fire = Spell("Fire", 5, 10, "elemental")
water = Spell("Water", 2, 4, "elemental")
earth = Spell("Earth", 3, 6, "elemental")
heal = Spell("Heal", 5, 5, "nature")

magicc = [fire, water, earth, heal]

#create items
potion = Item("Potion", "potion", "Heals 10 hp", 10)

elixer = Item("Elixer", "elixer", "Fully restores HP/MP of a party member", 100000)

grenade = Item("Grenade", "attack", "Deals 10 damage", 10)

player_items = [potion, elixer, grenade]

#create players
player1 = Person(1, 20, 10, 5, 5, magicc, "Player1", bcolors.OKGREEN, player_items, -1)

player2 = Person(1, 20, 10, 5, 5, [], "Player2", bcolors.OKBLUE, [], -1)

#create enemies
enemy = Person(3, 15, 0, 3, 2, [], "Enemy", bcolors.FAIL, [], 10)

running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

player = player1

while running:
    print("-------------------------")
    enemy.print_stats()
    player.print_stats()
    print("====================")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_dmg()
        dmg_taken = enemy.take_dmg(dmg)
        print(player.name, "attacked for:", dmg_taken, "points of damage")

    elif index == 1:
        if player.choose_magic() == -1:
            continue
        else:
            magic_choice = int(input("Choose magic: ")) - 1
            if magic_choice + 1 > int(len(player.magic)):
                print("You don't have that spell")
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_dmg(player)
            cost = spell.cost

            current_mp = player.get_mp()

            if cost > current_mp:
                print(bcolors.FAIL + "\n Not Enough MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(cost)

            if spell.typee == ("nature" or "light"):
                player.heal(magic_dmg)
                print(player.name, "healed for: ", magic_dmg, "points of HP. Current HP: ", bcolors.OKGREEN +
                      str(player.get_hp()) + "/" + str(player.get_maxhp()) + bcolors.ENDC)
            else:
                enemy.take_dmg(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

    elif index == 2:
        if player.choose_item() == -1:
            continue
        else:
            item_choice = int(input("Choose item: ")) - 1
            if item_choice + 1 > int(len(player.items)):
                print("You don't own that item")
                continue

            item = player.items[item_choice]
            item_val = item.prop

            if item.type == "potion":
                player.heal(item_val)
                print(player.name, "healed for: ", item_val, "points of HP. Current HP: ",
                      bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_maxhp()) + bcolors.ENDC)

            elif item.type == "attack":
                enemy.take_dmg(item_val)
                print(item.name, "hits for: ", item_val, "points of HP")

            elif item.type == "elixer":
                player.hp = player.maxhp
                print(player.name, "restored to full HP. Current HP: ",
                      bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_maxhp()) + bcolors.ENDC)

    else:
        continue

    if enemy.get_hp() == 0:

        lvl_diff = player.get_char_level() - enemy.get_char_level()
        xp_inc = enemy.get_xp_val() - int(lvl_diff * 0.25 * enemy.get_xp_val())
        if xp_inc <= 0:
            xp_inc = 0
        print(bcolors.OKGREEN + "You won!" + bcolors.ENDC + " +" + str(xp_inc) + "XP gained")
        player.xp_increase(xp_inc)
        player.print_stats()
        running = False
    else:
        enemy_choice = 1
        enemy_dmg = enemy.generate_dmg()
        dmg_taken = player.take_dmg(enemy_dmg)
        print(enemy.name, "attacked for:", dmg_taken , "points of damage")

    if player.get_hp() == 0:
        print(bcolors.FAIL + "You have been defeated" + bcolors.ENDC)
        enemy.print_stats()
        player.print_stats()
        running = False
