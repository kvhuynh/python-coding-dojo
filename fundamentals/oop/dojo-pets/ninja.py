import pets as Pet

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

benji = Pet.Pet("Benji", "Frenchie", "Sit", 100, 100)
kevin = Ninja("Kevin", "Huynh", benji, "treat", "kibble")
kevin.display_stats()
kevin.feed().walk().bathe()
kevin.display_stats()


cat = Pet.AnotherPet("Bob", "Siamese", "Run", 100, 100)
susan = Ninja("Susan", "Huynh", cat, "treat", "wet food")
susan.display_stats()
susan.feed().walk().bathe()
susan.display_stats()