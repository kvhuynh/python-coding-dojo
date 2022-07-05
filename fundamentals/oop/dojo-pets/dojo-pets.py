class Ninja(): 
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    
    def display_stats(self):
        print(self.pet.energy)
        print(self.pet.health)

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

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

benji = Pet("Benji", "Frenchie", "Sit", 100, 100)
kevin = Ninja("Kevin", "Huynh", benji, "treat", "kibble")
kevin.display_stats()
kevin.feed().walk().bathe()
kevin.display_stats()