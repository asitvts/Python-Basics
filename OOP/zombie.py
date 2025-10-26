from enemy import *

class Zombie(Enemy):

    def __init__(self, health, damage):
        super().__init__("zombie",health,damage)
        self.health = health
        self.damage = damage

    def attack(self):
        print(f"{self.type} is attacking right now grrrrr, damage inflicted is {self.damage}")

