class Enemy:

# __ added for mangling

    def __init__(self, type, health, damage):
        self.type = type
        self.health = health
        self.damage = damage

    def attack(self):
        print(f"{self.type} is attacking right now, damage inflicted is {self.damage}")

    def getHealth(self):
        print(f"current health of {self.type} is {self.health}")


