from enemy import *
from weapon import *


class Hero(Enemy):
    def __init__(self, health, damage):
        super().__init__("Hero", health, damage)
        self.health = health
        self.damage = damage

    def equipWeapon(self, weapon: Weapon):
        self.damage+=weapon.damage


    def attack(self):
        print(f"{self.type} is attacking right now (HAAAAA), damage inflicted is {self.damage}")

