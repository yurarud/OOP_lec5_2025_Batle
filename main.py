import random


class Person:
    def __init__(self, name, life, damage, shield):
        self.name = name
        self.life = life
        self.damage = damage
        self.shield = shield

    def is_alive(self):
        return self.life > 0

    def print_status(self):
        print(f"{self.name}: HP={self.life}, DMG={self.damage}, SH={self.shield}")

    def attack(self, other):
        if not self.is_alive() or not other.is_alive():
            return

        damage_dealt = max(1, self.dealt_damage() - other.create_shield())  # Мінімальний урон - 1
        other.life -= damage_dealt
        print(f"{self.name} атакує {other.name} та завдає {damage_dealt} урону!")

        if not other.is_alive():
            print(f"{other.name} загинув!")

    def dealt_damage(self):
        pass

    def create_shield(self):
        pass



class Warrior(Person):
    def __init__(self, name):
        super().__init__(name, random.randint(80, 120), random.randint(20, 50), random.randint(10, 30))
        self.harddamage = random.randint(5, 15)

    def create_shield(self):
        return self.shield

    def dealt_damage(self):
        return self.damage + self.harddamage


class Mage(Person):
    def __init__(self, name):
        super().__init__(name, random.randint(50, 90), random.randint(25, 55), random.randint(5, 20))
        self.supershield = random.randint(5, 15)

    def create_shield(self):
        return self.shield + self.supershield

    def dealt_damage(self):
        return self.damage


class Battleground:
    def __init__(self, num_heroes=3):
        self.command1 = []
        self.command2 = []
        self.create_teams(num_heroes)

    def create_teams(self, num_heroes):
        for i in range(num_heroes):
            self.command1.append(Warrior(f"Warrior_{i + 1}")) if random.choice([True, False]) else self.command1.append(
                Mage(f"Mage_{i + 1}"))
            self.command2.append(Warrior(f"Warrior_{i + 1 + num_heroes}")) if random.choice(
                [True, False]) else self.command2.append(Mage(f"Mage_{i + 1 + num_heroes}"))
        for i in self.command1:
            i.print_status()
        for i in self.command2:
            i.print_status()


    def battle(self):
        round_number = 1
        while self.has_alive(self.command1) and self.has_alive(self.command2):
            print(f"\n=== Раунд {round_number} ===")
            self.fight_round()
            round_number += 1

        winner = "Команда 1" if self.has_alive(self.command1) else "Команда 2"
        print(f"Перемогла {winner}!")

    def fight_round(self):
        self.command1 = [hero for hero in self.command1 if hero.is_alive()]
        self.command2 = [hero for hero in self.command2 if hero.is_alive()]

        for attacker in self.command1:
            if self.command2:
                defender = random.choice(self.command2)
                attacker.attack(defender)

        self.command2 = [hero for hero in self.command2 if hero.is_alive()]

        for attacker in self.command2:
            if self.command1:
                defender = random.choice(self.command1)
                attacker.attack(defender)

        self.command1 = [hero for hero in self.command1 if hero.is_alive()]

    def has_alive(self, team):
        return any(hero.is_alive() for hero in team)


if __name__ == "__main__":
    battleground = Battleground()#num_heroes=3
    battleground.battle()
