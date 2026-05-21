class Tamagochi: 
    def __init__(self, name):
        self.name = name
        self.age = 1
        self.hunger = 100
        self.happiness = 100

    def timepassed(self) :
        self.age += 1
        self.hunger -= 10
        self.happiness -= 10
        if self.hunger <= 0 :
            return f"{self.name} dies of starvation."
        elif self.happiness <= 0 :
            return f"{self.name} dies of boredom"
        else :
            return f"{self.name} aged!"
    def feed(self) :
        if self.hunger > 80 :
            return f"{self.name} is not hungry right now."
        else :
            self.hunger += 20
            return f"{self.name} ate."

    def play(self) :
        if self.happiness > 80 :
            return f"{self.name} is not in the mood to play."
        else :
            self.happiness += 20
            return f"{self.name} enjoyed playing!"