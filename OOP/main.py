from enemy import *
from zombie import *
from ogre import *
from hero import *
from weapon import *


zombie = Zombie(100,80)

zombie.attack()
zombie.getHealth()


print()

ogre = Ogre(100,110)
ogre.attack()
ogre.getHealth()


hero = Hero(100,50)


# polymorphism
def battle(en: Enemy):
    en.attack()



print("battling")
battle(ogre)
battle(zombie)
battle(hero)

weapon = Weapon("Sword",500)
hero.equipWeapon(weapon)
battle(hero)