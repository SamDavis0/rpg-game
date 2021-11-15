import random


class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def alive(self):
        if self.health > 0:
            return True

    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.damage} damage.")

    def attack(self, enemy):
        print('~' * 40)
        attack_chance = random.randint(1, 10)
        enemy.take_damage(self.damage)

    def take_damage(self, damage):
        if self.name == 'Shadow':
            dodge_chance = random.randint(1, 10)
            if dodge_chance == 1:
                self.health -= damage
        else:
            self.health -= damage
        print("\n")
        print(f'{self.name} takes {damage} damage!')
        if self.health <= 0:
            print(f"{self.name} has perished.")


class Hero(Character):
    def __init__(self, name, health, damage, gold):
        self.name = name
        self.health = health
        self.damage = damage
        self.gold = gold
        self.inventory = {}
        self.evade = 0
        self.armor = 0

    def restore(self, amt_health):
        self.health += amt_health


    def attack(self, enemy):
        print('~' * 40)
        attack_chance = random.randint(1, 10)
        if attack_chance >= 8:
            self.damage *= 2
            print(f"You landed a critical hit on the {enemy.name}!")
        enemy.take_damage(self.damage)

    def take_damage(self, damage):
        actual_evade = hero.evade
        if actual_evade > 20:
            actual_evade = 20
        rand_num = random.randint(1, 100)
        if rand_num >= actual_evade:
            if self.armor > 0:
                self.armor -= damage
                if self.armor < 0:
                    self.armor = 0
            else:
                self.health -= damage
        print(f"{self.name} takes {damage} damage")

    def purchase(self, item):
        self.gold -= item.cost

class Medic(Character):
    def __init__(self, name, health, damage, bounty):
        self.name = name
        self.health = health
        self.damage = damage
        self.bounty = bounty
        # sometimes can recoop 2 health points after being attack @ 20% prob

    def healing(self):
        healing_chance = random.randint(1, 10)
        if healing_chance >= 8:
            self.health += 20
            print(f'{self.name} healed 20 points!')


class Pickpocket(Character):
    def __init__(self, name, health, damage, bounty):
        self.name = name
        self.health = health
        self.damage = damage
        self.bounty = bounty
        # you cannot attack him + he steals your coins
        # is only accessable after you have coins


class Goblin(Character):
    def __init__(self, name, health, damage, bounty):
        self.name = name
        self.health = health
        self.damage = damage
        self.bounty = bounty   # 100


class Gremlin(Character):
    def __init__(self, name, health, damage, bounty):
        self.name = name
        self.health = health
        self.damage = damage
        self.bounty = bounty   # 50
        # misses its attack 25% of the time


class Zombie(Character):
    def __init__(self, name, health, damage, bounty):
        self.name = name
        self.health = health
        self.damage = damage
        self.bounty = bounty   # 1000
        # does not die
    def take_damage(self, damage):
        print("Oh no! Zombie isn't taking damage! You must fleeeeeeee")


class Shadow(Character):
    def __init__(self, name, health, damage, bounty):
        self.name = name
        self.health = health
        self.damage = damage
        self.bounty = bounty   # 500


class SuperTonic(object):  # restores to full health
    def __init__(self):
        self.cost = 500
        self.name = 'super tonic!'

    def apply(self, hero):
        hero.restore(90)
        print(f"{hero.name}'s health increased to {hero.health}.")


class Armor(object):  # adds 10 armor points
    def __init__(self):
        self.cost = 150
        self.name = 'armor of protection'

    def apply(self, hero):
        hero.armor += 10
        print(f"{hero.name}'s armor increased to {hero.armor}.")


class Evade(object):  # adds 2 evade points ~2 evade points = 10%   4 = 15%
    def __init__(self):
        self.cost = 150
        self.name = 'cloak of evasion'

    def apply(self, hero):
        hero.evade += 2
        print(f"{hero.name}'s evade increased to {hero.evade}.")


class Potion(object):  # turns you into a llama
    def __init__(self):
        self.cost = 20
        self.name = "a mysterious purple potion"

    def apply(self, hero):
        print(
            f"You fool! That was the poison. The poison for Kuzco, the poison chosen especially to kill Kuzco, Kuzco's poison! {hero.name} is now a llama.")
        raise SystemExit


class Food(object):  # gives you 5 health points
    def __init__(self):
        self.cost = 50
        self.name = 'some food'

    def apply(self, hero):
        hero.restore(5)
        print(
            f"{hero.name} eats Green Eggs and Ham. {hero.name}'s health increased to {hero.health}.")


class Shop(object):
    items = [SuperTonic(), Armor(), Evade(), Potion(), Food()]

    def shopping(hero):
        while True:
            print("\n")
            print("~" * 40)
            print("Welcome to our store!")
            print("~" * 40)
            print(f'You have {hero.gold} gold.')
            print("What would you like to do?")

            for i in range(len(Shop.items)):
                item = Shop.items[i]
                print(f"{i + 1}. Buy {item.name} ({item.cost})")

            print("6. leave")
            choice = int(input("> "))

            if choice == 6:
                break

            else:
                items_to_buy = Shop.items[choice - 1]
                item = items_to_buy
                if hero.gold >= items_to_buy.cost:
                    hero.purchase(item)

                    if item.name in hero.inventory:
                        hero.inventory[item.name].append(item)
                    else:
                        hero.inventory[item.name] = [item]

                    print(
                        f"You have obtained {item.name}. You have {len(hero.inventory[item.name])} of {item.name}.")
                    print(f"Would you like to use {item.name}? (Y/N)")
                    print("> ", end=' ')
                    answer = input().upper()
                    if answer == 'Y':
                        hero.inventory[item.name][0].apply(hero)
                        hero.inventory[item.name].pop()
                    else:
                        continue
                else:
                    print(
                        f"You must have {items_to_buy.cost} gold to buy a {items_to_buy.name}")


class Combat(object):
    def mid_battle_menu():
        print('~' * 40)
        print(f"What do you want to do?\n1. Slap him.\n2. Really? Nothing?\n3. Run!")
        print("> ", end=' ')


    def battle_menu(hero, enemy):
        print('~' * 40)
        print(
            f"You stumble across {enemy.name} based off their convenient name tag.")
        print('~' * 40)
        print("\n")

        hero.print_status()
        enemy.print_status()
        print(f"What do you want to do?\n1. Slap him.\n2. Really? Nothing?\n3. Run!")
        print("> ", end=' ')

        # while (enemy.alive() && hero.alive() && hero.in_battle === true)

        while enemy.alive() and hero.alive():
            answer = int(input())
            if answer == 1:
                hero.attack(enemy)
                enemy.print_status()
                if enemy.alive():
                    enemy.attack(hero)
                hero.damage = 10
                hero.print_status()
                Combat.mid_battle_menu()
            elif answer == 2:
                enemy.attack(hero)
                Combat.mid_battle_menu()
            elif answer == 3:
                print("Your pants fall down running away.")
                return
            else:
                print("Try again.")
        if hero.alive():
            print('~' * 30)
            print(f"You defeated {enemy.name}!")
            hero.gold += enemy.bounty
            print(
                f'{hero.name} recieved {enemy.bounty} gold for defeating {enemy.name}!')
            return


class Instance(object):
    def main_menu(hero, enemy_list):
        while hero.alive():
            print('~' * 40)
            # if hero.gold > 0:
            print(
                f"What do you want to do?\n1. Go for a fight \n2. Sleep?\n3. Commit sudoku\n4. Go shopping!")
            # else:
            #     print(
            #         f"What do you want to do?\n1. Go for a fight\n2. Sleep?\n3. Commit sudoku")
            print("> ", end=' ')
            answer = int(input())
            if answer == 1:
                Combat.battle_menu(hero, enemy_list[random.randint(0, 5)])
            elif answer == 2:
                print('~' * 40)
                print("Okay nap time!")
                pass
            elif answer == 3:
                print("YOU COWARD")
                break
            elif answer == 4:
                if hero.gold > 0:
                    Shop.shopping(hero)
                else:
                    print("You have no gold :(")
            else:
                print(f"Everyone deserves a chance to try again!")


if __name__ == "__main__":
    hero = Hero("Bobby", 100, 10, 0)
    medic = Medic("Priest Boi", 100, 5, 150)
    thief = Pickpocket("Slobby Rob", 100, 5, 500)
    goblin = Goblin("Cheese", 100, 10, 100)
    gremlin = Gremlin("Taco", 100, 10, 50)
    zombie = Zombie("Tim", 100, 10, 200)
    shadow = Shadow("Lucky", 1, 10, 100)

    enemy_list = [medic, thief, goblin, gremlin, zombie, shadow]

    Instance.main_menu(hero, enemy_list)