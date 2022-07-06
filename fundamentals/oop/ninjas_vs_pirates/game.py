from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

michelangelo.attack(jack_sparrow)
jack_sparrow.show_stats()

i = 100
while i != 0:
    if michelangelo.health > 0 or jack_sparrow.health > 0:
        michelangelo.attack(jack_sparrow)
        jack_sparrow.show_stats()
        input()
        jack_sparrow.attack(michelangelo)
        michelangelo.show_stats()
        i -= 1

    else:
        print("The battle is over!")
        if michelangelo.health > jack_sparrow.health:
            print(michelangelo.name + "  wins!")
        else:
            print(jack_sparrow.name + "  wins!")

        break
