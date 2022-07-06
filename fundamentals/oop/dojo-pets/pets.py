class Pet():
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    
    def sleep(self):
        self.energy += 25

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        return "woof"


class AnotherPet(Pet):
    def __init__(self, name, type, tricks, health, energy):
        super().__init__(name, type, tricks, health, energy)
    
    def sleep(self):
        self.energy += 2500000

    def eat(self):
        self.energy += 500000
        self.health += 100000
        return self

    def play(self):
        self.health += 10000
        return self

    def noise(self):
        return "meow"