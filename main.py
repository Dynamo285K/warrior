class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack
        self.is_alive = True if health > 0 else False

class Knight(Warrior):
    def __init__(self, health=50, attack=7):
        super().__init__(health, attack)
        # Warrior.__init__(self,health, attack)

class Army:
    def __init__(self):
        self.units = []

    def add_units(self, warrior, count):
        self.units.extend([warrior() for i in range(count)])

class Battle:
    def fight(army1, army2):
        while army1.units and army2.units:
            army1_unit = army1.units.pop(0)
            army2_unit = army2.units.pop(0)

            while army1_unit.is_alive and army2_unit.is_alive:
                army2_unit.health -= army1_unit.attack
                army2_unit.is_alive = True if army2_unit.health > 0 else False

                if army2_unit.is_alive:
                    army1_unit.health -= army2_unit.attack
                    army1_unit.is_alive = True if army1_unit.health > 0 else False
                else:
                    break

            if army1_unit.is_alive:
                army1.units.append(army1_unit)
            else:
                army2.units.append(army2_unit)

        return bool(army1.units)

def fight(fighter1, fighter2):
    if not fighter1.is_alive:
        return False
    if not fighter2.is_alive:
        return True

    while fighter1.is_alive and fighter2.is_alive:
        fighter2.health -= fighter1.attack
        if fighter2.health <= 0:
            fighter2.is_alive = False
            return True

        fighter1.health -= fighter2.attack
        if fighter1.health <= 0:
            fighter1.is_alive = False
            return False


# chuck = Warrior()
# bruce = Warrior()
# carl = Knight()
# dave = Warrior()
# mark = Warrior()
#
# print(fight(chuck, bruce)) == True
# print(fight(dave, carl)) == False
# print(chuck.is_alive) == True
# print(bruce.is_alive) == False
# print(carl.is_alive) == True
# print(dave.is_alive) == False
# print(fight(carl, mark)) == False
# print(carl.is_alive) == False


my_army = Army()
my_army.add_units(Knight, 3)

enemy_army = Army()
enemy_army.add_units(Warrior, 3)

army_3 = Army()
army_3.add_units(Warrior, 20)
army_3.add_units(Knight, 5)

army_4 = Army()
army_4.add_units(Warrior, 30)

# battle = Battle()

print(Battle.fight(my_army, enemy_army)) == True
print(Battle.fight(army_3, army_4)) == False

# chuck = Warrior()
# bruce = Warrior()
# carl = Knight()
# dave = Warrior()
# mark = Warrior()
#
# print(fight(chuck, bruce)) == True
# print(fight(dave, carl)) == False
# print(chuck.is_alive) == True
# print(bruce.is_alive) == False
# print(carl.is_alive) == True
# print(dave.is_alive) == False
# print(fight(carl, mark)) == False
# print(carl.is_alive) == False

# army1 = Army()
# army1.add_units(Warrior, 1)
#
# army2 = Army()
# army2.add_units(Knight, 2)
#
# battle_result = Battle.fight(army1, army2)
# print("Army 1 won!" if battle_result else "Army 2 won!")



# chuck = Warrior()
# bruce = Warrior()
# carl = Knight()
# dave = Warrior()
#
# print(fight(chuck, bruce)) == True
# print(fight(dave, carl)) == False
# print(chuck.is_alive) == True
# print(bruce.is_alive) == False
# print(carl.is_alive) == True
# print(dave.is_alive) == False






