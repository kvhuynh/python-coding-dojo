import random
class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        attack_bonus = random.randint(1,2)
        # crit
        if attack_bonus == 1:
            pirate.health -= self.strength * 2
            print(self.name + "landed a critical hit!")           
        else:
            pirate.health -= self.strength
        return self