import random
class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        attack_bonus = random.randint(1,2)
        # crit
        if attack_bonus == 1:
            ninja.health -= self.strength * 2
            print(self.name + "landed a critical hit!")
        else:
            ninja.health -= self.strength
        return self

