#from enemy import *
from zombie import *
from ogre import *


zombie = Zombie(100,80)

zombie.attack()
zombie.getHealth()


print()

ogre = Ogre(100,110)
ogre.attack()
ogre.getHealth()