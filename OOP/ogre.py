from enemy import *

class Ogre(Enemy):
    def __init__(self, health, damage):
        super().__init__("Ogre", health, damage)
        self.health=100
        self.damage=110

    def attack(self):
        print(f"{self.type} is attacking right now Ugh Ugh, damage inflicted is {self.damage}")
